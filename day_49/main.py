import os
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)
    raise TimeoutException(f"{description} failed after {retries} retries")

def open_schedule(driver, wait):
    driver.get(GYM_URL_SCHEDULE)
    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

def click_and_confirm_button_text(wait, button, expected_text: str):
    button.click()
    wait.until(lambda d: button.text.strip() == expected_text)

def open_my_bookings(driver, wait):
    link = wait.until(ec.element_to_be_clickable((By.ID, "my-bookings-link")))
    link.click()

    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards

def main():
    # Start a driver of Chrome
    driver = make_driver()
    wait = WebDriverWait(driver, 10)

    # Browse Gym page
    driver.get(GYM_URL)

    # Log in to homepage
    # Go to Schedule page
    retry(lambda: login(driver, wait), description="login")
    # Wait for schedule page to load
    retry(lambda: open_schedule(driver, wait), description="open schedule")

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


    # --- Book Upcoming Tuesday or Thursday Class at 6 pm ---

    # Find all class cards
    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
    counts = {
        "booked": 0,
        "waitlisted": 0,
        "already": 0,
        "unknown": 0,
    }

    rules = {
        "Booked": ("✓ Already booked", False, "already", "[Booked]", None),
        "Waitlisted": ("✓ Already on waitlist", False, "already", "[Waitlisted]", None),
        "Book Class": ("✓ Successfully booked", True, "booked", "[New Booked]", "Booked"),
        "Join Waitlist": ("✓ Joined waitlist", True, "waitlisted", "[New Waitlist]", "Waitlisted"),
    }

    processed_classes = []

    for card in class_cards:
        # Get the day title from the parent day group
        day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        # Check if this is a Tuesday
        if "Tue" in day_title or "Thu" in day_title:
            # Check if this is a 6pm class
            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            if "6:00 PM" in time_text:
                # Get the class name
                class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

                button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

                status = button.text.strip()
                class_info = f"{class_name} on {day_title}"

                msg, should_click, bucket, process, expected_text = rules.get(
                    status,
                    ("? Unknown button state", False, "unknown", "[Unknown]", None)
                )
                print(f"{msg}: {class_name} on {day_title}")
                counts[bucket] += 1
                processed_classes.append(f"{process} {class_info}")

                if should_click:
                    retry(
                        lambda: click_and_confirm_button_text(wait, button, expected_text),
                        description=f"{status} -> {expected_text} ({class_info})"
                    )
                    time.sleep(0.5)


    expected_total = counts["booked"] + counts["waitlisted"] + counts["already"]

    # print("\n--- BOOKING SUMMARY ---")
    # print(f"Classes booked: {counts['booked']}")
    # print(f"Waitlists joined: {counts['waitlisted']}")
    # print(f"Already booked/waitlisted: {counts['already']}")
    # print(f"Unknown states: {counts['unknown']}")

    # print("\n--- DETAILED CLASS LIST ---")
    # for class_detail in processed_classes:
    #     print(f"  • {class_detail}")

    print(f"\n--- Total Tuesday & Thursday 6pm classes processed: {expected_total} ---")
    print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

    # Go to My Booking page
    all_cards = retry(lambda: open_my_bookings(driver, wait), description="open my bookings")

    # Count all Tue/Thu 6 pm bookings
    verified_count = 0


    for card in all_cards:
        try:
            when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
            when_text = when_paragraph.text

            if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
                class_name = card.find_element(By.TAG_NAME, "h3").text
                print(f"  ✅ Verified: {class_name}")
                verified_count += 1
        except NoSuchElementException:
            # If no "When:" skip
            pass

    print(f"\n--- VERIFICATION RESULTS ---")
    print(f"Expected: {expected_total} bookings")
    print(f"Found: {verified_count} bookings")

    if expected_total == verified_count:
        print("✅ SUCCESS: All bookings verified")
    else:
        print(f"❌ FAILURE: Missing {expected_total - verified_count} bookings")

if __name__ == '__main__':
    main()
