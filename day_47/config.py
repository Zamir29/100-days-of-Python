import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- Testing Page ---
BREWERY_URL = "https://appbrewery.github.io/instant_pot/"
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
USER_AGENT = os.getenv("USER_AGENT")
# ---

# --- Price configuration ---
PRICE_THRESHOLD = 120
# ---

# --- GMAIL SMTP ---
GMAIL_SMTP = os.getenv("GMAIL_SMTP")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
ZCH_MAIL = os.getenv("ZCH_MAIL")
# ---