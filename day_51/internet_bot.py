import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from config import (
    SPEEDTEST_URL,
    X_EMAIL,
    X_PASSWORD,
    X_URL,
)

class InternetSpeedXBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.timeout_default = 10
        self.wait = WebDriverWait(self.driver, self.timeout_default)
        self.down = 0
        self.up = 0

    def cookie_popup_reject(self):
        try:
            cookie_reject = self.wait.until(
                ec.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))

            )
            cookie_reject.click()
        except TimeoutException:
            pass

    def read_speed(self, selector, label):
        try:
            load_value = self.wait.until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, selector))
            )
        except TimeoutException:
            raise TimeoutException(f"The element was not visible within {self.timeout_default} seconds")

        start_time = time.time()
        timeout_seconds = 60
        print(f"📋 Checking the {label} speed") #, end="", flush=True)
        while True:
            # Replace dot so only numbers remain, and replace only the first dot, if there are more it is invalid anyway
            raw_text = load_value.text.strip()
            check_text = raw_text.replace(".", "", 1)
            if check_text.isdigit():
                value = float(raw_text)
                if value > 0:
                    print(f"\n✅ Done in {(time.time() - start_time):.2f} seconds\n")
                    return value

            if time.time() - start_time > timeout_seconds:
                raise TimeoutException(f"Speed value did not become a valid number within {timeout_seconds} seconds")

            print(".", end="", flush=True) # Print without newline end, flush=True means write immediately
            time.sleep(0.2)



    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        self.cookie_popup_reject()
        go_button = self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "a.js-start-test"))
        )
        go_button.click()

        # Find download value
        self.down = self.read_speed(selector="span.download-speed", label="Download")

        # Find upload value
        self.up = self.read_speed(selector="span.upload-speed", label="Upload")

        return self.down, self.up

    def x_at_provider(self, complaint_text):
        # Go directly to the login page
        self.driver.get(X_URL)

        # Input username
        input_username = self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "input[autocomplete='username']"))
        )
        input_username.send_keys(X_EMAIL)

        # Click Enter
        input_username.send_keys(Keys.ENTER)

        # Input Password
        input_password = self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "input[autocomplete='current-password']"))
        )
        input_password.send_keys(X_PASSWORD)

        # Click Enter
        input_password.send_keys(Keys.ENTER)

        # Tweet Text editor
        tweet_box = self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']"))
        )

        # Activate the box to input text
        tweet_box.click()

        # Input tweet text
        tweet_box.send_keys(complaint_text)

        # # Send tweet
        # tweet_box.send_keys(Keys.ENTER)

        # Alternative of Post button
        post_tweet = self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']"))
        )
        post_tweet.click()


    def driver_quit(self):
        self.driver.quit()