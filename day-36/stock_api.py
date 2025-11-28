import requests

# TODO: define StockAPI class
# TODO: implement get_closing_prices()
# TODO: implement get_diff()
# TODO: error handling
# TODO: tests

class StockAPI:

    def __init__(self, api_key, ticker):
        self.api_key = api_key
        self.ticker = ticker
        self.endpoint_url = "https://www.alphavantage.co/query"

    def get_closing_prices(self):
        """Fetch last 2 closing prices from API"""
        pass

    def get_diff(self, price1, price2):
        """Compute percentage difference"""
        pass
