import requests
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    ElementNotInteractableException,
    StaleElementReferenceException, TimeoutException,
)

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

    @staticmethod
    def pick_visible_input(item, item_index):
        selector_list = [
            "div[role='heading'] span",
            "input, textarea",
        ]
        try:
            elements = item.find_elements(By.CSS_SELECTOR, selector_list[item_index])
            return next((element for element in elements if element.is_displayed() and element.is_enabled())
                        , None)
        except StaleElementReferenceException:
            return None

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

        item_filled = 0
        all_items_filled = False
        # Loops through items
        for item in form_items:

            # Scroll question into view to help Google Forms render the label/input
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", item)

            # Label check and get the value
            label = self.pick_visible_input(item, item_index=0)
            if label is None or not label.text.strip():
                try:
                    label = WebDriverWait(driver, 4).until(
                        lambda d: self.pick_visible_input(item, item_index=0)
                    )
                except TimeoutException:
                    # Can't map this questions without its label
                    continue

            label = label.text.strip().lower()
            if not label or label not in align_params:
                continue

            key = align_params[label]
            value = data_dict.get(key, "")

            input_item = self.pick_visible_input(item, item_index=1)

            if input_item is None:
                try:
                    input_item = WebDriverWait(driver, 4).until(
                        lambda d: self.pick_visible_input(item, item_index=1)
                    )
                except TimeoutException:
                    print(f"⚠️ No visible input for label: {label}")
                    continue

            # Retries for three times to input the value
            for attempt in range(3):
                if input_item is None:
                    time.sleep(0.2)
                    input_item = self.pick_visible_input(item, item_index=1)
                    continue

                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_item)
                    input_item.click()
                    input_item.clear()
                    input_item.send_keys(value)
                    item_filled += 1
                    time.sleep(0.2)
                    break
                except (ElementNotInteractableException, StaleElementReferenceException, InvalidElementStateException):
                    if attempt == 2:
                        print(f"❌ Could not type into filed '{label}' after retries")
                        break
                    time.sleep(0.2)
                    # re-find after DOM update
                    # candidates = item.find_elements(By.CSS_SELECTOR, "input, textarea")
                    # input_item = next(
                    #     (element for element in candidates if element.is_displayed() and element.is_enabled()),
                    #     None
                    # )
                    input_item = self.pick_visible_input(item, item_index=1)
                    continue

        if item_filled >= len(align_params):
            all_items_filled = True

        buttons = wait.until(
            ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[aria-label='Submit'], div[aria-label='Invia']")
            )
        )
        buttons.click()

        time.sleep(0.2)

        driver.quit()

        return all_items_filled