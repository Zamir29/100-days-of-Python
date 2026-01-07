from selenium import webdriver
from config import (
    PROMISED_UP,
    PROMISED_DOWN,
    X_EMAIL,
    X_PASSWORD,
)

class InternetSpeedXBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def x_at_provider(self):
        pass