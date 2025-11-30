import os
from news_api import NewsAPI

COMPANY_NAME = "Tesla Inc"

def main():
    api_key = os.getenv("NEWS_API")
    print(f"API key loaded? {api_key is not None}")
    from_date = "2025-11-28"

    last_news = NewsAPI(
        api_key=api_key,
        query=COMPANY_NAME,
        from_date=from_date
    )

    three_articles, get_url = last_news.get_news()

    print(three_articles)
    print(get_url)

if __name__ == "__main__":
    main()