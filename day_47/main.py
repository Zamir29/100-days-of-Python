from bs4 import BeautifulSoup
import requests
import smtplib
from config import (
    BREWERY_URL,
    AMAZON_URL,
    PRICE_THRESHOLD,
    GMAIL_SMTP,
    MY_PASSWORD,
    MY_EMAIL,
    ZCH_MAIL,
)

def get_item_data():
    # Using the URL from Angela
    url_brewery = BREWERY_URL
    url_amazon = AMAZON_URL

    # Get the whole
    response = requests.get(url=url_brewery)
    # print(response.status_code)

    # Create the soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the item price
    full_price = soup.find(class_="aok-offscreen").get_text().split()[0]
    currency = full_price[0]
    price = float(full_price[1:])

    # Get the item title
    product_title = soup.find(id="productTitle").get_text().strip().split()
    product_title = " ".join(product_title)

    return currency, price, product_title, url_amazon

def send_email(message):
    with smtplib.SMTP(host=GMAIL_SMTP,
                      port=587,
                      timeout=30
                      ) as connection:  # adding the port number solves the idle
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD
        )
        connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=ZCH_MAIL,
                msg=f"Subject:[Alert] Lower Price on Amazon\n\n{message}"
            )

def main():
    currency, price, product_title, url_amazon = get_item_data()
    message = (f"Oh wow! The price for\n'{product_title}'\nis {price}, below the {PRICE_THRESHOLD} by {price/PRICE_THRESHOLD*100:.2f}%!!\n"
               f"GO and by it: {url_amazon}").encode("utf-8")

    if price < PRICE_THRESHOLD:
        send_email(message)
    else:
        print(f"Sorry, the price of '{product_title}' is still higher than {PRICE_THRESHOLD}.")
if __name__ == '__main__':
    main()
