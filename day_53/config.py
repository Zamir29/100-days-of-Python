import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- ZILLOW CLONE ---
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
# ----

# --- GOOGLE FORM ---
GOOGLE_FORM_URL = "https://forms.gle/Z94MpFX3qecRgurdA"
# ---

# --- REQUEST HEADER ---
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}
# ---