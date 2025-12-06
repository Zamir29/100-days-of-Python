import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- SHEETY API ---

# Sheety Token
SHEETY_KEY = os.getenv("SHEETY_KEY")

# Sheety API key
SHEETY_BEARER_KEY = f"Bearer {SHEETY_KEY}"

# Sheety API url
SHEETY_GET = "https://api.sheety.co/3ddb00ef84d1e4724f8af231f008a342/flightDeals/prices"
SHEET_POST = "https://api.sheety.co/3ddb00ef84d1e4724f8af231f008a342/flightDeals/prices"

# ---

# --- AMADEUS API ---

# Amadeus Key, Secret, Token
AMADEUS_KEY = os.getenv("AMADEUS_KEY")
AMADEUS_SECRET = os.getenv("AMADEUS_SECRET")

# Amadeus API Url
AMADEUS_POST = "https://test.api.amadeus.com/v1/security/oauth2/token"
