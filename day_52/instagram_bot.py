import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

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

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass