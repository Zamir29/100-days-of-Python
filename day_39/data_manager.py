import pandas as pd
import requests

from config import SHEETY_BEARER_KEY, SHEETY_GET, SHEET_POST

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.key = SHEETY_BEARER_KEY
        self.get_url = SHEETY_GET
        self.post_url = SHEET_POST
        self.headers = {"Authorization": SHEETY_BEARER_KEY,}

    def get_table(self):

        response = requests.get(url=self.get_url, headers=self.headers)

        get_data = response.json()
        worksheet_name = list(get_data.keys())[0]

        get_rows = get_data[f"{worksheet_name}"]

        prices_df = pd.DataFrame.from_dict(get_rows)

        return prices_df, get_rows, response

    def put_to_table(self):

        # need what
        # need where
        pass