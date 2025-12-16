import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

load_dotenv(find_dotenv())

# --- ONGOING YEAR ---
THIS_YEAR = datetime.today().year

# ---

# --- WIKIPEDIA Billboard Year-end 100 singles list ---
USER_AGENT = os.environ.get("USER_AGENT")
BILLBOARD_LISTS_URL = "https://en.wikipedia.org/wiki/Category%3ALists_of_Billboard_Year-End_Hot_100_singles"
BILLBOARD_URL = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_"
# ---
