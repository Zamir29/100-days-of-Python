import requests
import re
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url: str, headers: dict, timeout: int = 15):
        self.url = url
        self.headers = headers
        self.timeout = timeout
        self.currency = "$"

    def fetch(self) -> str:
        response = requests.get(url=self.url, headers=self.headers, timeout=self.timeout)
        response.raise_for_status()
        site_html = response.text

        return site_html

    @staticmethod
    def parse(html: str):
        return BeautifulSoup(html, "html.parser")

    def get_list(self, soup):
        result_container = soup.select_one(selector="div.result-list-container ul")

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


    def get_item_data(self, one_item):
        # Focus on the <a> tag that contains link and address
        get_a = one_item.select_one("a[data-test='property-card-link']")

        if not get_a:
            return None

        # Retrieve the address
        address_tag = get_a.select_one("address")
        get_address = address_tag.get_text(strip=True) if address_tag else ""

        # Retrieve the link
        get_link = get_a.get("href", "")

        # Retrieve the price tag
        price_tag = one_item.select_one("span[data-test='property-card-price']")
        price_raw = price_tag.get_text(strip=True) if price_tag else ""
        if not price_raw:
            return None

        # get_price = ""
        # for char in price_raw:
        #     if char.isdigit() or char in ("$", ",", "."):
        #         get_price += char

        # Match the pattern using the price raw output
        match = re.search(r"(\d[\d,]*\.?\d*)", price_raw)
        if not match:
            return None

        # Create the price as required by Angela to input in the Google Form
        number_str = match.group(1)
        get_price = f"{self.currency}{number_str}"

        data_dict = {
            "address": get_address,
            "price": get_price,
            "link": get_link,
        }

        return data_dict

    def run(self) -> list[dict[str, str]]:
        html = self.fetch()
        soup = self.parse(html=html)
        return self.get_list(soup=soup)