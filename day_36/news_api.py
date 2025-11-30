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
        params = {
            "apiKey": self.api_key,
            "q": self.query,
            "from": self.from_date,
            "sortBy": "publishedAt",
            "pageSize": 3,
            "page": 1,
        }

        response = requests.get(url=self.endpoint_url, params=params)
        response.raise_for_status()
        # get_url = response.url

        # Get news data with the last three articles
        news_data = response.json()

        get_articles = news_data["articles"]

        three_articles = [
            {
                "headline": news["title"],
                "brief": news["description"],
                "url": news["url"],
                "media": news["urlToImage"],
                "date": news["publishedAt"],

            }
            for news in get_articles[:3]

        ]

        return three_articles
