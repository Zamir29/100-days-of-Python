from config import (
    AMADEUS_SECRET,
    AMADEUS_KEY,
    AMADEUS_POST
)
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.client_id = AMADEUS_KEY
        self.client_secret = AMADEUS_SECRET
        self.post_url = AMADEUS_POST

    def get_amadeus_token():
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        user_params = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_KEY,
            "client_secret": AMADEUS_SECRET,
        }

        amadeus_response = requests.post(url=AMADEUS_POST, data=user_params, headers=headers)
        amadeus_response.raise_for_status()

        return amadeus_response.json()["access_token"]

