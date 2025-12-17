import requests
from bs4 import BeautifulSoup
from config import (
    AMAZON_URL,
    USER_AGENT,
)

def get_item_data():
    # Using the URL from Angela
    url_amazon = AMAZON_URL

    headers = {
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US,en;q=0.5",
    }

    # Get the whole
    response = requests.get(url=url_amazon, headers=headers)
    response.raise_for_status()
    # Create the soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the item title
    title_tag = soup.find(id="productTitle")

    if not title_tag:
        print("No title tag found")
        return None

    product_title = " ".join(title_tag.get_text().strip().split())

    # Get price form span.a-price-# and from .aok_offscreen
    price_container = soup.select_one(selector="#corePriceDisplay_desktop_feature_div") or soup
    full_price_tag = price_container.select_one(selector=".aok-offscreen")

    symbol_tag = price_container.select_one(selector="span.a-price-symbol")
    whole_tag = price_container.select_one(selector="span.a-price-whole")
    fraction_tag = price_container.select_one(selector="span.a-price-fraction")

    symbol = symbol_tag.get_text(strip=True) if symbol_tag else None
    whole = whole_tag.get_text(strip=True).replace(".", "").replace(",", "") if whole_tag else None
    fraction = fraction_tag.get_text(strip=True).replace(".", "").replace(",", "") if fraction_tag else None

    if whole and fraction:
        return symbol, float(f"{whole}.{fraction}"), product_title, url_amazon
    elif full_price_tag:
        parts = full_price_tag.get_text().split()
        symbol = parts[0]
        price = float(parts[1])
        return symbol, price, product_title, url_amazon
    else:
        print("No price foud for this item.")
        return None


def main():
    print(get_item_data())

if __name__ == "__main__":
    main()