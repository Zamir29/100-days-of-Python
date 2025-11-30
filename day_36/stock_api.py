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
        """Return (latest_close, previous_close) as floats from the daily time series."""

        parameters = {
            "function": self.function,
            "symbol": self.ticker,
            "apikey": self.api_key,
            "outputsize": "compact", # this is the default for Free Members
            "datatype": "json", # json is the default, alternative csv
        }

        response = requests.get(url=self.endpoint_url, params=parameters)
        response.raise_for_status() # error handling, in case it won't work

        # Get the json from AlphaVantage.co
        data = response.json()

        # Get the dictionary with the daily trades
        series = data["Time Series (Daily)"]
        dates = sorted(series.keys(), reverse=True) # Descending order to have the last date on position 0 in the list

        # Find the keys of lastest date and previous
        last_date = dates[0]
        prev_date = dates[1]

        # Get the string from the series dictionary
        last_closing_str = series[last_date]["4. close"]
        prev_closing_str = series[prev_date]["4. close"]

        # Transform the string to float
        last_close = float(last_closing_str)
        prev_close = float(prev_closing_str)

        return last_close, prev_close, prev_date

    def get_diff(self, price_now, price_prev):
        """
        Compute percentage difference between current and previous price.

        Args:
            price_now: latest closing price.
            price_prev: previous closing price.

        Returns:
            (sign, abs_percentage_diff)
            sign = "🔺" if price went up, "🔻" if it went down.
        """

        # Get the price difference
        p_now = float(price_now)
        p_prev = float(price_prev)

        if p_prev == 0:
            raise ValueError("price_prev must not be zero")

        diff = p_now - p_prev

        # Get the percentage and sign
        percentage = (diff/p_prev) * 100 # can be negative

        sign = "🔺" if percentage >= 0 else "🔻"

        return sign, abs(percentage)



        pass
