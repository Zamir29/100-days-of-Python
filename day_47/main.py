from bs4 import BeautifulSoup
from config import (
    BREWERY_URL,
)
import requests

def get_price():
    url = BREWERY_URL
    response = requests.get(url=url)
    print(response.status_code)

    soup = BeautifulSoup(response.content, "html.parser")

    full_price = soup.find(class_="aok-offscreen").get_text().split()[0]
    currency = full_price[0]
    price = float(full_price[1:])

    return currency, price

def main():
    print(get_price())

if __name__ == '__main__':
    main()
