from selenium import webdriver
import os

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Reference to the expected condition: https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_support/selenium.webdriver.support.expected_conditions.html#selenium.webdriver.support.expected_conditions.element_to_be_clickable


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

def is_logged_in(driver, timeout: int = 2) -> bool:
    """Return TRUE if UI shows the Logout button (meaning we are logged in)."""
    try:
        WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((By.ID, "logout-button"))
        )
        return True
    except TimeoutException:
        return False

def login(driver, wait):
    """
    Log in only if the user is currently logged out."""
    # Defensive check: if .env vars are missing, fail fast with a clear message
    if not GYM_USER or not GYM_PASSWORD:
        raise ValueError(
            "Missing credentials. Check that .env is present and loaded into config.py"
        )

    # If already logged in (e.g. Chrome profile kept the session), do nothing.
    if is_logged_in(driver):
        print("You are already logged in 💪")
        return

    # If not logged in, Find Log in button because it should exist
    try:

        login_btn = wait.until(
            ec.element_to_be_clickable((By.ID, "login-button"))
        )
    except TimeoutException:
        # Sometimes the page is slow, or we landed on a page where login isn't shown
        if is_logged_in(driver):
            return
        raise

    login_btn.click()

    # Input email
    input_email = wait.until(
        ec.visibility_of_element_located((By.ID, "email-input"))
    )
    input_email.clear()
    input_email.send_keys(GYM_USER)

    # Input password
    input_password = wait.until(
        ec.visibility_of_element_located((By.ID, "password-input"))
    )
    input_password.clear()
    input_password.send_keys(GYM_PASSWORD)

    # Submit login
    login_submit = wait.until(
        ec.element_to_be_clickable((By.ID, "submit-button"))
    )

    login_submit.click()

    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "logout-button"))
    )

def main():
    # Start a driver of Chrome
    driver = make_driver()
    wait = WebDriverWait(driver, 10)

    # Browse Gym page
    driver.get(GYM_URL)

    # Log in to homepage
    login(driver, wait)

    # Go to Schedule page
    driver.get(GYM_URL_SCHEDULE)

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
    # a[href *= "insensitive"i] {
    #     color: cyan;
    # }
    #
    # Links that end in ".org"
    # a[href$=".org"] {
    #     color: red;
    # }

    # Wait for schedule page to load
    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

    # --- Book Upcoming Tuesday Class at 6 pm ---

    # Find all class cards
    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

    for card in class_cards:
        # Get the day title from the parent day group
        day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        # Check if this is a Tuesday
        if "Tue" in day_title:
            # Check if this is a 6pm class
            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            if "6:00 PM" in time_text:
                # Get the class name
                class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

                button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

                status = button.text.strip()

                rules = {
                    "Booked": ("✓ Already booked", False),
                    "Waitlisted": ("✓ Already on waitlist", False),
                    "Book Class": ("✓ Successfully booked", True),
                    "Join Waitlist": ("✓ Joined waitlist", True),
                }

                msg, should_click = rules.get(status, ("? Unknown button state", False))
                print(f"{msg}: {class_name} on {day_title}")

                if should_click:
                    button.click()

                if status in rules:
                    break


if __name__ == '__main__':
    main()
