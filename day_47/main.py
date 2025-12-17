from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
from config import (
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

def send_email(message):
    # To avoid any ascii error using email that is safer
    email = EmailMessage()
    email["From"] = MY_EMAIL
    email["To"] = ZCH_MAIL
    email["Subject"] = "[Alert] Lower Price on Amazon"
    email.set_content(message)

    with smtplib.SMTP(host=GMAIL_SMTP,
                      port=587,
                      timeout=30
                      ) as connection:  # adding the port number solves the idle
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD,
        )
        connection.send_message(email)

def main():
    symbol, price, product_title, url_amazon = get_item_data()
    message = (f"Oh wow!\n\nThe price for\n'{product_title}'\n\nis {symbol} {price}\n\n"
               f"below the {PRICE_THRESHOLD} by {(PRICE_THRESHOLD-price)/PRICE_THRESHOLD*100:.2f}%!!\n"
               f"GO and buy it: {url_amazon}")

    if price < PRICE_THRESHOLD:
        send_email(message)
    else:
        print(f"Sorry, the price of '{product_title}' is still higher than {PRICE_THRESHOLD}.")
if __name__ == '__main__':
    main()
