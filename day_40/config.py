import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- SHEETY API ---

# Sheety Token
SHEETY_KEY = os.getenv("SHEETY_KEY")

# Sheety API key
SHEETY_BEARER_KEY = f"Bearer {SHEETY_KEY}"

# Sheety API url
SHEETY_PRICES_GET = "https://api.sheety.co/3ddb00ef84d1e4724f8af231f008a342/flightDeals/ggg"
SHEETY_PRICES_POST = "https://api.sheety.co/3ddb00ef84d1e4724f8af231f008a342/flightDeals/ggg"
SHEETY_PRICES_PUT = "https://api.sheety.co/3ddb00ef84d1e4724f8af231f008a342/flightDeals/ggg"

SHEETY_USERS_GET = "https://api.sheety.co/3ddb00ef84d1e4724f8af231f008a342/flightDeals/users"
SHEETY_USERS_POST = "https://api.sheety.co/3ddb00ef84d1e4724f8af231f008a342/flightDeals/users"
SHEETY_USERS_PUT = "https://api.sheety.co/3ddb00ef84d1e4724f8af231f008a342/flightDeals/users"

# ---

# --- AMADEUS API ---

# Amadeus Key, Secret, Token
AMADEUS_KEY = os.getenv("AMADEUS_KEY")
AMADEUS_SECRET = os.getenv("AMADEUS_SECRET")

# Amadeus API Url
AMADEUS_URL = "https://test.api.amadeus.com/"
AMADEUS_URL_TOKEN = f"{AMADEUS_URL}v1/security/oauth2/token"
AMADEUS_URL_GET_DEAL = f"{AMADEUS_URL}v1/shopping/flight-destinations"
AMADEUS_URL_CHEAPEST_DATE = f"{AMADEUS_URL}v1/shopping/flight-dates"
AMADEUS_URL_AIRPORT_CITY_SEARCH = f"{AMADEUS_URL}v1/reference-data/locations"

# ---

# --- TWILIO API ---

# Twilio Key, Token
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")

# Twilio whatsapp sandbox numbers
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
TWILIO_WHATSAPP_TO = os.getenv("TWILIO_WHATSAPP_TO")