from config import (
    AMADEUS_SECRET,
    AMADEUS_KEY,
    AMADEUS_URL_TOKEN,
    AMADEUS_URL_GET_DEAL
)
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.client_id = AMADEUS_KEY
        self.client_secret = AMADEUS_SECRET
        self.url_get_token = AMADEUS_URL_TOKEN
        self.url_get_deal = AMADEUS_URL_GET_DEAL

    def get_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        user_params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        amadeus_response = requests.post(url=self.url_get_token, data=user_params, headers=headers)
        amadeus_response.raise_for_status()

        return amadeus_response.json()["access_token"]

    def find_deals(self):
        # , origin: str, map_price: str
        headers = {
            "Authorization": f"Bearer {self.get_token()}",
        }

        params = {
            "origin": "PAR",
            "maxPrice": 200,
        }

        deals_response = requests.get(url=self.url_get_deal, params=params, headers=headers)

        return deals_response
