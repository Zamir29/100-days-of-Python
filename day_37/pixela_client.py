import requests
from config import (
    PIXELA_BASE_URL,
    PIXELA_USERNAME,
    PIXELA_TOKEN,
    PIXELA_GRAPH_ID,
)


def create_user():
    """Run this once at the beginning"""
    # Find more info on https://docs.pixe.la/entry/post-user#Request-Body
    user_params = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=PIXELA_BASE_URL, json=user_params)

    return response