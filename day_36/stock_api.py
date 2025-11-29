import requests

# TODO: define StockAPI class
# TODO: implement get_closing_prices()
# TODO: implement get_diff()
# TODO: error handling
# TODO: tests

class StockAPI:
    DEFAULT_FUNCTION = "TIME_SERIES_DAILY"

    def __init__(self, api_key, ticker, function=None):
        self.api_key = api_key
        self.ticker = ticker
        self.function = function or self.DEFAULT_FUNCTION
        self.endpoint_url = "https://www.alphavantage.co/query"

    def get_closing_prices(self):
        """Fetch last 2 closing prices from API"""

        parameters = {
            "function": self.function,
            "symbol": self.ticker,
            "apikey": self.api_key,
            "outputsize": "compact", # this is the default for Free Members
            "datatype": "json", # json is the default, alternative csv
        }

        response = requests.get(url=self.endpoint_url, params=parameters)
        response.raise_for_status() # error handling, in case it won't work

        return response.json()

    def get_diff(self, price1, price2):
        """Compute percentage difference"""
        pass
