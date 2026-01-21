""" Config keeps all the data used in the app"""
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- NPOINT JSON WITH POSTS ---
NPOINT_URL = "https://api.npoint.io/35d4767901d354fcdde6"
# ---

# --- GMAIL SMTP ---
GMAIL_SMTP = os.getenv("GMAIL_SMTP")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
ZCH_MAIL = os.getenv("ZCH_MAIL")
# ---
