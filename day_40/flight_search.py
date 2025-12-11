from config import (
    AMADEUS_SECRET,
    AMADEUS_KEY,
    AMADEUS_URL_TOKEN,
    AMADEUS_URL_GET_DEAL,
    AMADEUS_URL_CHEAPEST_DATE,
    AMADEUS_URL_AIRPORT_CITY_SEARCH,
)
from flight_data import FlightData
import requests
from datetime import datetime, timedelta

# Available API for test https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/test-data/
class FlightSearch:
    """Client for interacting with the Amadeus Flight APIs.

        This class:
        - Retrieves OAuth tokens from Amadeus.
        - Searches for cheapest flight dates and prices between two locations.
        - Looks up IATA city codes from city names.
    """
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        """Initialize the FlightSearch client with configuration and date window.

        The search window is set from "tomorrow" up to roughly six months from now.
        """
        self.client_id = AMADEUS_KEY
        self.client_secret = AMADEUS_SECRET
        self.url_get_token = AMADEUS_URL_TOKEN
        self.url_get_deal = AMADEUS_URL_GET_DEAL # Used to do the first test as in Docs
        self.url_cheapest_date = AMADEUS_URL_CHEAPEST_DATE
        self.url_airport_city = AMADEUS_URL_AIRPORT_CITY_SEARCH
        self.tomorrow = datetime.now() + timedelta(days=1)
        self.six_months = self.tomorrow + timedelta(days=6*365/12)

    def get_token(self):
        """Request an OAuth access token from Amadeus.

        Uses the `client_credentials` flow as described in the Amadeus docs.

        Returns:
            The access token string.

        Raises:
            requests.HTTPError: If the Amadeus token endpoint returns a non-2xx status.
        """
        # --- TOKEN API --- -> https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/API-Keys/authorization/
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        user_params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        # Use "data" as on Docs it refers to the 'x-www-form-urlencoded'
        amadeus_response = requests.post(url=self.url_get_token, data=user_params, headers=headers)
        amadeus_response.raise_for_status()

        return amadeus_response.json()["access_token"]

    def find_deals(self, origin_code: str, destination_code: str, max_price: float, is_direct=True, ):
        """Find the cheapest flight within a date range under a maximum price.

        Uses the "Flight Cheapest Date Search" Amadeus endpoint.
        The date range is from `self.tomorrow` up to `self.six_months`.

        Args:
            origin_code: IATA code of the origin city/airport (e.g. "MIL").
            destination_code: IATA code of the destination city/airport (e.g. "PAR").
            max_price: Maximum acceptable price (in the currency returned by Amadeus).
            is_direct: if True only direct flights, otherwise flights with stops in between will be considered

        Returns:
            A `FlightData` instance representing the best deal found.

        Raises:
            ValueError: If the Amadeus API returns a non-OK response,
                if no flights are returned,
                or if no flight is cheaper than `max_price`.
        """
        # --- Flight Cheapest Date API --> https://developers.amadeus.com/self-service/category/flights/api-doc/flight-cheapest-date-search

        # Retrieve automatically the date of Tomorrow and in Six months
        tomorrow = self.tomorrow.strftime("%Y-%m-%d")
        six_months = self.six_months.strftime("%Y-%m-%d")
        non_stop = "true" if is_direct else "false"

        headers = {
            "Authorization": f"Bearer {self.get_token()}",
        }

        params = {
            "origin": origin_code,
            "destination": destination_code,
            "departureDate": f"{tomorrow},{six_months}",
            "oneWay": True, # Can be set to false, but then "duration: str" should be set
            "nonStop": non_stop,
            "maxPrice": max_price,

        }

        deals_response = requests.get(url=self.url_cheapest_date, params=params, headers=headers)

        if not deals_response.ok:
            msg = f"Amadeus Error: {deals_response.status_code},{deals_response.text}"
            raise ValueError(msg)

        deal_list = deals_response.json()["data"]

        # This runs if deal_list is empty and is_direct=True, to look to indirect flights
        if not deal_list and is_direct:
            params["nonStop"] = "false"
            deals_response = requests.get(url=self.url_cheapest_date, params=params, headers=headers)

            if not deals_response.ok:
                msg = f"Amadeus Error: {deals_response.status_code},{deals_response.text}"
                raise ValueError(msg)

            deal_list = deals_response.json()["data"]

        # If everything fails, then give up
        if not deal_list:
            raise ValueError("No flights found for given parameters")

        best_price = None
        best_deal = None
        for deal in deal_list:
            price = float(deal["price"]["total"])
            if price <= max_price:
                if best_price is None or price < best_price:
                    best_price = price
                    best_deal = deal

        if best_deal is None:
            raise ValueError(f"No flight from {origin_code} to {destination_code} between {tomorrow} and {six_months} is below {max_price}")


        return FlightData(price=float(best_deal["price"]["total"]),
                          departure_code=best_deal["origin"],
                          arrival_code=best_deal["destination"],
                          departure_date=best_deal["departureDate"],
                          start_date=tomorrow,
                          end_date=six_months)

    def get_iata_code(self, city_name: str):
        """Look up the IATA city code for a given city name.

        Uses the Amadeus "Airport & City Search" endpoint with `subType="CITY"`.

        Args:
            city_name: Human-readable city name (e.g. "Paris", "Tokyo").

        Returns:
            The IATA location code for the city (e.g. "PAR").

        Raises:
            ValueError: If the API returns an empty `data` list,
                meaning no IATA code was found for the given city.
            requests.HTTPError: If the Amadeus API returns a non-2xx status.
        """
        # --- Airport & City Search API --- -> https://developers.amadeus.com/self-service/category/flights/api-doc/airport-and-city-search/api-reference
        headers = {
            "Authorization": f"Bearer {self.get_token()}",
        }

        params = {
            "subType": "CITY", # Another option is "AIRPORT", always uppercase
            "keyword": city_name,
            "view": "LIGHT", # Another option is "FULL", always uppercase

        }

        airport_city_response = requests.get(url=self.url_airport_city, params=params, headers=headers)
        airport_city_response.raise_for_status()
        data = airport_city_response.json()["data"]

        if not data:
            raise ValueError(f"No IATA code found for city: {city_name}")

        # Take the first match
        return data[0]["iataCode"]