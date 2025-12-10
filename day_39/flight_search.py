from config import (
    AMADEUS_SECRET,
    AMADEUS_KEY,
    AMADEUS_URL_TOKEN,
    AMADEUS_URL_GET_DEAL,
    AMADEUS_URL_CHEAPEST_DATE,
    AMADEUS_URL_AIRPORT_CITY_SEARCH,
)
import requests
from datetime import datetime, timedelta

# Available API for test https://developers.amadeus.com/self-service/apis-docs/guides/developer-guides/test-data/
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.client_id = AMADEUS_KEY
        self.client_secret = AMADEUS_SECRET
        self.url_get_token = AMADEUS_URL_TOKEN
        self.url_get_deal = AMADEUS_URL_GET_DEAL # Used to do the first test as in Docs
        self.url_cheapest_date = AMADEUS_URL_CHEAPEST_DATE
        self.url_airport_city = AMADEUS_URL_AIRPORT_CITY_SEARCH
        self.tomorrow = datetime.now() + timedelta(days=1)
        self.six_months = self.tomorrow + timedelta(days=6*365/12)

    def get_token(self):
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

    def find_deals(self, origin_code: str, destination_code: str, max_price: int):
        # --- Flight Cheapest Date API --> https://developers.amadeus.com/self-service/category/flights/api-doc/flight-cheapest-date-search

        # Retrive automatically the date of Tomorrow and in Six months
        tomorrow = self.tomorrow.strftime("%Y-%m-%d")
        six_months = self.six_months.strftime("%Y-%m-%d")

        headers = {
            "Authorization": f"Bearer {self.get_token()}",
        }

        params = {
            "origin": origin_code,
            "destination": destination_code,
            "departureDate": f"{tomorrow},{six_months}",
            "oneWay": True, # Can be set to false, but then "duration: str" should be set
            "maxPrice": max_price,

        }

        deals_response = requests.get(url=self.url_cheapest_date, params=params, headers=headers)

        return deals_response

    def get_iata_code(self, city_name: str):
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