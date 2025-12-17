import requests
from bs4 import BeautifulSoup
from config import (
    BREWERY_URL,
    AMAZON_URL,
    PRICE_THRESHOLD,
    GMAIL_SMTP,
    MY_PASSWORD,
    MY_EMAIL,
    ZCH_MAIL,
    USER_AGENT,
)

def get_item_data():
    # Using the URL from Angela
    url_brewery = BREWERY_URL
    url_amazon = AMAZON_URL

    headers = {
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US,en;q=0.5",
    }

    # Get the whole
    response = requests.get(url=url_amazon, headers=headers)
    # print(response.status_code)

    # Create the soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the item price
    full_price = soup.find(class_="aok-offscreen").get_text().split()
    # print(full_price)
    currency = full_price[0]
    price = float(full_price[1])

    # print(currency, price)
    # Get the item title
    product_title = soup.find(id="productTitle").get_text().strip().split()
    product_title = " ".join(product_title)

    return currency, price, product_title, url_amazon


def main():
    print(get_item_data())

if __name__ == "__main__":
    main()