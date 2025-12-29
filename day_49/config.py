import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- Gym Page ---
GYM_USER = os.getenv("GYM_USER")
GYM_PASSWORD = os.getenv("GYM_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym"
GYM_URL_SCHEDULE = f"{GYM_URL}/schedule/"
# ---