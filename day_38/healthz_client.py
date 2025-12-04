import requests
from datetime import datetime
from config import (
    X_APP_KEY,
    X_APP_ID,
    X_APP_URL,
    X_APP_GET,
    X_APP_POST,
    ERROR_CODE,
    SHEETY_BEARER_KEY,
    SHEET_POST,
    SHEETY_GET,
)

def get_exercise_stats(get_query):

    query_params = {
        "query": get_query,
    }

    headers = {
        "X-APP-ID": X_APP_ID,
        "X-APP-KEY": X_APP_KEY,
    }

    response = requests.post(url=X_APP_POST, json=query_params, headers=headers)

    return response

def add_activity(response):
    data = response["exercises"][0]

    activity_params = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": data["name"],
            "duration": data["duration_min"],
            "calories": data["nf_calories"],
        },
    }

    headers = {
        "Authorization": SHEETY_BEARER_KEY,
    }

    response = requests.post(url=SHEET_POST, json=activity_params, headers=headers)

    return response