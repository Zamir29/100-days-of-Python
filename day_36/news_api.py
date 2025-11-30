import requests

class NewsAPI:

    def __init__(self, api_key, query, from_date):
        self.api_key = api_key
        self.query = query
        self.from_date = from_date
        self.endpoint_url = "https://newsapi.org/v2/everything"

    def get_news(self):
        """
        Starting from a query returns three last news from a date.
        The news are structured with a title(Headline),a brief description, date published and url
        """
        parameter = {
            "apiKey": self.api_key,
            "q": self.query,
            "from": self.from_date,
            "sortBy": "publishedAt",
            "pageSize": 3,
            "page": 1,
        }

        pass
