import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from config import (
    INSTA_USERNAME,
    INSTA_PASSWORD,
    # SIMILAR_ACCOUNT,
)
class InstaFollower:
    def __init__(self):
        # Keep Chrome browser open after program finishes
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # Create user data directory
        user_data_dir = os.path.join(os.getcwd(), "insta_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.timeout_default = 10
        self.wait = WebDriverWait(self.driver, self.timeout_default)
        self.url = "https://www.instagram.com/accounts/login/"

    def login(self):
        self.driver.get(self.url)
        try:
            decline_cookies = self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Decline')]"))
            )
            if decline_cookies:
                decline_cookies.click()
        except TimeoutException:
            pass

        # Log in
        username = self.wait.until(
            ec.element_to_be_clickable((By.NAME, 'username'))
        )
        username.click()
        username.send_keys(INSTA_USERNAME)

        password = self.wait.until(
            ec.element_to_be_clickable((By.NAME, 'password'))
        )
        password.click()
        password.send_keys(INSTA_PASSWORD)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

        # Use keywords "decline" "Not now"
        for _ in range(2):
            try:
                not_now = self.wait.until(
                    ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not now')]")))
                not_now.click()
                time.sleep(1)
            except TimeoutException:
                break


    def find_followers(self):
        pass

    def follow(self):
        pass