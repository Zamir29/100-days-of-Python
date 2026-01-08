import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- INSTAGRAM CREDENTIALS ---
SIMILAR_ACCOUNT = "chefsteps"
INSTA_USERNAME = os.getenv("INSTA_USERNAME")
INSTA_PASSWORD = os.getenv("INSTA_PASSWORD")
# ---