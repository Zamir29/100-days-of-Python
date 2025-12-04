import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

X_APP_URL = "https://app.100daysofpython.dev"

# Credentials of Nutrition API
X_APP_ID = os.getenv("X-APP-ID")
X_APP_KEY = os.getenv("X-APP-KEY")
