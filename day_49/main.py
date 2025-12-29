from selenium import webdriver
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from config import (
    GYM_USER,
    GYM_PASSWORD,
    GYM_URL,
    GYM_URL_SCHEDULE
)

def make_driver():

    # Keep Chrome browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # Create user data directory
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


    # Return a driver
    return webdriver.Chrome(options=chrome_options)

def login(wait):
    # Reference to the expected condition: https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_support/selenium.webdriver.support.expected_conditions.html#selenium.webdriver.support.expected_conditions.element_to_be_clickable
    # Find Log in
    login_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_btn.click()

    # Input email
    input_email = wait.until(
        EC.visibility_of_element_located((By.ID, "email-input"))
    )
    input_email.send_keys(GYM_USER)

    # Input password
    input_password = wait.until(
        EC.visibility_of_element_located((By.ID, "password-input"))
    )
    input_password.send_keys(GYM_PASSWORD)

    # Submit login
    login_submit = wait.until(
        EC.element_to_be_clickable((By.ID, "submit-button"))
    )
    login_submit.click()

def main():
    # Start a driver of Chrome
    driver = make_driver()
    wait = WebDriverWait(driver, 10)

    # Browse Gym page
    driver.get(GYM_URL)

    # Log in to homepage
    login(wait)

    # Go to Schedule page
    driver.get(GYM_URL_SCHEDULE)

    # Book the next event at 6pm
    day = "2025-12-24"
    hours = "1800"

    # Get the list of day groups
    card_specific = driver.find_element(By.CSS_SELECTOR, f"div[id$='{day}-{hours}']")
    # How to select by partial text
    # / *Internal
    # links, beginning with "#"
    # a[href ^= "#"] {
    #         background - color: gold;
    #     }
    #
    # Links with "example" anywhere in the URL
    # a[href *= "example"] {
    #         background - color: silver;
    #     }
    #
    # Links with "insensitive" anywhere in the URL, regardless of capitalization
    # a[href *= "insensitive"
    # i] {
    #     color: cyan;
    # }
    #
    # Links that end in ".org"
    # a[href$=".org"] {
    #     color: red;
    # }
    button = card_specific.find_element(By.CSS_SELECTOR, "button")
    button.click()

    print(card_specific)



if __name__ == '__main__':
    main()
