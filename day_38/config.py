import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

X_APP_URL = "https://app.100daysofpython.dev"

# Credentials of Nutrition API
X_APP_ID = os.getenv("X-APP-ID")
X_APP_KEY = os.getenv("X-APP-KEY")

# API urls
X_APP_POST = f"{X_APP_URL}/v1/nutrition/natural/exercise"
X_APP_GET = f"{X_APP_URL}/healthz"

# Error code
ERROR_CODE = {
    "401": {
        "Error Code": "UNAUTHENTICATED",
        "Description": "Missing or invalid API credentials",
    },
    "422": {
        "Error Code": "INVALID_REQUEST",
        "Description": "Request validation failed (check required fields)",
    },
    "429": {
        "Error Code": "RATE_LIMIT_EXCEEDED",
        "Description": "Too many requests (max 60/minute)",
    },
    "500": {
        "Error Code": "INTERNAL_ERROR",
        "Description": "Server error",
    },

}