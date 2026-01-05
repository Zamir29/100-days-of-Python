from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from config import (
    FACEBOOK_EMAIL,
    FACEBOOK_PASSWORD,
)

def wait_click(wait, by, selector):
    return wait.until(ec.element_to_be_clickable((by, selector))).click()

def wait_find(wait, by, selector):
    return wait.until(ec.presence_of_element_located((by, selector)))

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.tinder.com")

    login_button = wait.until(
        ec.element_to_be_clickable((By.XPATH, '//*[text()="Log In"]'))
    )
    login_button.click()

    fb_login = wait.until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button'))
    )
    fb_login.click()

    # Select Facebook login window pop up
    wait.until(ec.number_of_windows_to_be(2))
    base_window = driver.current_window_handle # Not using index to avoid any scrambling

    # Pick the first of all the windows that are different from base_window
    fb_login_window = [w for w in driver.window_handles if w != base_window][0]
    driver.switch_to.window(fb_login_window)
    print(driver.title)

    # Login and click enter
    email = wait.until(
        ec.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))
    )
    password = wait.until(
        ec.visibility_of_element_located((By.XPATH, '//*[@id="pass"]'))
    )
    email.send_keys(FACEBOOK_EMAIL)
    password.send_keys(FACEBOOK_PASSWORD)
    password.send_keys(Keys.ENTER)

    # Switch back to Tinder window
    driver.switch_to.window(base_window)
    print(driver.title)

    sleep(5)

    allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]]')
    allow_location_button.click()

    notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
    notifications_button.click()

    cookies_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    cookies_button.click()

    # Tinder limit 100:
    for n in range(100):
        # Add one-second delay between likes
        sleep(1)

        try:
            print("called")
            like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            like_button.click()

        # If It's a Match window pops up
        except ElementClickInterceptedException:
            try:
                match_popup = driver.find_element(By.CSS_SELECTOR, value='.itsAMatch a')
                match_popup.click()

            # Catches the cases where the "Like" button has not yet loaded
            except NoSuchElementException:
                sleep(2)

    driver.quit()

if __name__ == '__main__':
    main()
