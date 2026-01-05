from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from config import (
    FACEBOOK_EMAIL,
    FACEBOOK_PASSWORD,
)


def main():
    driver = webdriver.Chrome()

    driver.get("https://www.tinder.com")

    sleep(2)
    login_button = driver.find_element(By.XPATH, value='//*[text()="Log In"]')
    login_button.click()

    sleep(2)
    fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb_login.click()

    # Select Facebook login window pop up
    sleep(2)
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title)

    # Login and click enter
    email = driver.find_element(By.XPATH, value='//*[@id="email"]')
    password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
    email.send_keys(FACEBOOK_EMAIL)
    password.send_keys(FACEBOOK_PASSWORD)
    password.send_keys(Keys.ENTER)

    # Switch back to Tinder window
    driver.switch_to.window(base_window)
    print(driver.title)

if __name__ == '__main__':
    main()
