from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
from config import (
    # BREWERY_URL,
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
    # url_brewery = BREWERY_URL
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
    currency = full_price[0]
    price = float(full_price[1])

    # Get the item title
    product_title = soup.find(id="productTitle").get_text().strip().split()
    product_title = " ".join(product_title)

    return currency, price, product_title, url_amazon

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
    currency, price, product_title, url_amazon = get_item_data()
    message = (f"Oh wow!\n\nThe price for\n'{product_title}'\n\nis {currency} {price}\n\nbelow the {PRICE_THRESHOLD} by {(PRICE_THRESHOLD-price)/PRICE_THRESHOLD*100:.2f}%!!\n"
               f"GO and buy it: {url_amazon}")

    if price < PRICE_THRESHOLD:
        send_email(message)
    else:
        print(f"Sorry, the price of '{product_title}' is still higher than {PRICE_THRESHOLD}.")
if __name__ == '__main__':
    main()
