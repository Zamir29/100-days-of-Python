import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/zamirhashorva/Development/chromedriver"
X_EMAIL = os.getenv("X_EMAIL")
X_PASSWORD = os.getenv("X_PASSWORD")