import requests
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from selenium.common.exceptions import TimeoutException

class Scraper:
    def __init__(self, url: str, headers: dict, timeout: int = 15):
        self.url = url
        self.headers = headers
        self.timeout = timeout
        self.currency = "$"

    def fetch(self) -> str:
        response = requests.get(url=self.url, headers=self.headers, timeout=self.timeout)
        response.raise_for_status()

        return response.text

    @staticmethod
    def parse(html: str) -> BeautifulSoup:
        return BeautifulSoup(html, "html.parser")

    def get_list(self, soup: BeautifulSoup) -> list[dict[str, str]]:
        result_container = soup.select_one(selector="div.result-list-container ul")

        if not result_container:
            print("Container is empty")
            return []

        # Get only the direct child of <ul> https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=find_all#the-recursive-argument
        item_list = result_container.find_all("li", recursive=False)

        all_items: list[dict[str, str]] = []
        for item in item_list:
            data = self.get_item_data(item)
            if data is not None:
                all_items.append(data)

        return all_items


    def get_item_data(self, one_item) -> dict[str, str] | None:

        # Focus on the <a> tag that contains link and address
        link_tag = one_item.select_one("a[data-test='property-card-link']")

        if not link_tag:
            return None

        # Retrieve the address
        address_tag = link_tag.select_one("address")
        address_text = address_tag.get_text(strip=True) if address_tag else ""

        # Retrieve the link
        listing_url = link_tag.get("href", "")

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
        price_text = f"{self.currency}{number_str}"

        return {
            "address": address_text,
            "price": price_text,
            "link": listing_url,
        }


    def run(self) -> list[dict[str, str]]:
        html = self.fetch()
        soup = self.parse(html)
        return self.get_list(soup)

class FormFiller:
    def __init__(self, url: str, timeout: int = 15):
        self.url = url
        self.timeout = timeout

    def create_webdriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, self.timeout)

        return driver, wait

    def fill_form(self, data_dict: dict[str, str]):

        # Map Google Form field labels -> your dict keys
        align_params = {
            "address": "address",
            "price/month": "price",
            "link": "link",
        }

        # Create driver and get Google Form url
        driver, wait = self.create_webdriver()
        driver.get(self.url)

        # Wait for the list of questions to be visible
        form_list = wait.until(
            ec.visibility_of_element_located(
                (By.CSS_SELECTOR, "form[method='post'] div[role='list']")
            )
        )

        # Create a list of the items to be filled
        form_items = form_list.find_elements(
            By.CSS_SELECTOR, "div[role='listitem']"
        )

        # Loops through items
        for item in form_items:

            #Find the label and compare to the Map
            label = item.find_element(By.CSS_SELECTOR, "div[role='heading'] span").text.strip().lower()
            print("Field label:", label)

            if label not in align_params:
                continue

            key = align_params[label]
            value = data_dict.get(key, "")

            input_item = item.find_element(By.CSS_SELECTOR, "input")
            input_item.click()
            input_item.send_keys(value)

        buttons = wait.until(
            ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[aria-label='Submit']")
            )
        )

        buttons.click()
        time.sleep(0.2)

        driver.quit()

        return