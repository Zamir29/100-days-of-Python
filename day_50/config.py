import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- Facebook Page ---
FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")
#___
