import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

PROMISED_DOWN = 1500
PROMISED_UP = 10
X_EMAIL = os.getenv("X_EMAIL")
X_PASSWORD = os.getenv("X_PASSWORD")
SPEEDTEST_URL = "https://www.speedtest.net"