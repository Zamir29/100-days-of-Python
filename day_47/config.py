import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- Testing Page ---
BREWERY_URL = "https://appbrewery.github.io/instant_pot/"
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
USER_AGENT = os.getenv("USER_AGENT")
# ---

# --- Price configuration ---
PRICE_THRESHOLD = 100
# ---