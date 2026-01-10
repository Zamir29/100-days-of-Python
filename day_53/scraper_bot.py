import requests
from bs4 import BeautifulSoup
from config import (
    GOOGLE_FORM_URL,
    ZILLOW_URL,
    REQUEST_HEADERS,
)


class Scraper:
    def __init__(self):
        response = requests.get(ZILLOW_URL, headers=REQUEST_HEADERS, timeout=20)
        response.raise_for_status()
        self.site_html = response.text
        self.soup = BeautifulSoup(self.site_html, "html.parser")

    def get_list(self):
        result_container = self.soup.select_one(selector="div.result-list-container ul")

        if not result_container:
            print("Container is empty")
            return []

        # Get only the direct child of <ul> https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=find_all#the-recursive-argument
        item_list = result_container.find_all("li", recursive=False)

        all_items = []
        for item in item_list:
            data = self.get_item_data(item)
            if data is not None:
                all_items.append(data)

        return all_items

    @staticmethod
    def get_item_data( one_item):
        # Focus on the <a> tag that contains link and address
        get_a = one_item.select_one("a[data-test='property-card-link']")

        if not get_a:
            return None

        # Retrieve the address
        address_tag = get_a.select_one("address")
        get_address = address_tag.get_text(strip=True) if address_tag else ""

        # Retrieve the link
        get_link = get_a.get("href", "")

        price_tag = one_item.select_one("span[data-test='property-card-price']")
        price_raw = price_tag.get_text(strip=True) if price_tag else ""
        get_price = ""
        for char in price_raw:
            if char.isdigit() or char in ("$", ",", "."):
                get_price += char

        data_dict = {
            "address": get_address,
            "price": get_price,
            "link": get_link,
        }

        return data_dict
