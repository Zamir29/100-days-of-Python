import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- Speedtest Page ---
SPEEDTEST_URL = "https://www.speedtest.net"
INTERNET_PROVIDER = "Speedy" # Just a dummy Internet Provider so ChatGPT won't get crazy it is not a real one
PROMISED_DOWN = 1500
PROMISED_UP = 10
# ---

# --- X.com Page ---
X_URL = "https://x.com/i/flow/login"
X_EMAIL = os.getenv("X_EMAIL")
X_PASSWORD = os.getenv("X_PASSWORD")
# ---