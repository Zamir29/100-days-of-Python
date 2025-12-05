import requests
from datetime import datetime
import pandas as pd
from config import (
    X_APP_KEY,
    X_APP_ID,
    X_APP_POST,
    SHEETY_BEARER_KEY,
    SHEET_POST,
    SHEETY_GET,
)
from day_35.main import response

sheety_headers = {
        "Authorization": SHEETY_BEARER_KEY,
    }

app_headers = {
    "X-APP-ID": X_APP_ID,
    "X-APP-KEY": X_APP_KEY,
}

def get_table(row):
    row = row.lower().strip()

    if row == "all":
        get_url = SHEETY_GET
    else:
        get_url = f"{SHEETY_GET}/{row}"

    # print(get_url)
    response = requests.get(url=get_url, headers=sheety_headers)

    get_data = response.json()
    worksheet_name = list(get_data.keys())[0]

    get_rows = get_data[f"{worksheet_name}"]

    # Get_row becomes a list
    if row != "all":
        get_rows = [get_rows]

    # Print the list
    activity_tab = pd.DataFrame.from_dict(get_rows)

    print(activity_tab)

    return response, len(get_rows)

def get_details():
    get_query = input("Tell me which exercise you did: ")
    query_params = {
        "query": get_query
    }

    more_details = input("Do you want to add more details?\n[Y]/[N]: ")

    if more_details.lower().strip() in ("n", "no"):
        return query_params
    else:
        weight_kg = input("What's your weight?\nkg: ")
        height_cm = input("What's your height?\ncm: ")
        age = input("What's your age?\nnumber: ")
        gender = input("What's your gender?\n[male][female]: ")
        query_params.update({
            "weight_kg": int(weight_kg),
            "height_cm": int(height_cm),
            "age": int(age),
            "gender": gender,
        })
        print(query_params)
        return query_params


def get_exercise_stats():

    query_params = get_details()

    response = requests.post(url=X_APP_POST, json=query_params, headers=app_headers)

    return response


def add_activity():
    exercise_stats = get_exercise_stats().json()
    data = exercise_stats["exercises"][0]

    activity_params = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"), # issue: on Google sheet this is a string not time
            "exercise": data["name"],
            "duration": data["duration_min"],
            "calories": data["nf_calories"],
        },
    }



    response = requests.post(url=SHEET_POST, json=activity_params, headers=sheety_headers)

    return response

def edit_activity():
    # Show all the table
    table_response, table_len = get_table("all")

    what_row = input("What row do you want to delete? ")
    while what_row not in range(table_len):
        what_row = input(f"Please input a number between 0 and {table_len}")
