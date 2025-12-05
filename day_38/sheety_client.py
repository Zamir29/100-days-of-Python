import requests
from healthz_client import get_exercise_stats
from datetime import datetime
import pandas as pd
from config import (
    SHEETY_BEARER_KEY,
    SHEET_POST,
    SHEETY_GET,
)

sheety_headers = {
        "Authorization": SHEETY_BEARER_KEY,
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

    return activity_tab, response, len(get_rows)

def add_activity():

    while True:
        stats_response = get_exercise_stats()

        if stats_response.status_code == 200:
            exercise_stats = stats_response.json()
            exercises = exercise_stats["exercises"]

            if len(exercises) == 0 or exercises[0]["name"] == "exercise" :
                print("Please use a format like 'ran for 30 minutes', 'jogged 2 miles'")
            else:
                break

        else:
            print(f"There was an issue {stats_response.status_code}: {stats_response.json()['message']}.\nLet's retry\n")



    now = datetime.now()
    add_response = None

    for exercise in exercises:
        activity_params = {
            "workout": {
                "date": now.strftime("%d/%m/%Y"),
                "time": now.strftime("%H:%M:%S"), # issue: on Google sheet this is a string not time
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            },
        }

        add_response = requests.post(url=SHEET_POST, json=activity_params, headers=sheety_headers)

    if add_response.status_code == 200:
        print("Done! It's there")
    else:
        print(f"Shoot! It says error {add_response.status_code}: {add_response.json()['message']}")

    return add_response

def edit_activity():
    # Show all the table
    all_table, _, table_len = get_table("all")
    print(all_table)

    # Select row
    while True:
        try:
            what_row = int(input("\nWhat row do you want to edit? "))
            if what_row in range(table_len):
                break  # Valid number, exit loop
            else:
                print(f"Please input a number between 0 and {table_len - 1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Calculate sheety ID
    sheety_row_id =all_table.iloc[what_row]["id"]

    # Show row preview
    row_df, row_response, _ = get_table(f"{sheety_row_id}")
    print(f"\nExpected row to edit\n{row_df}")

    # Dynamically extraxt the root key
    root_key = list(row_response.json().keys())[0]

    # Convert DataFrame to dict to start edit
    current_data = row_df.to_dict(orient="records")[0]

    # Confirm Edit
    while True:
        confirm = input("\nDo you confirm you want to edit this? [Y]/[N]: ").lower().strip()
        if confirm in ["n", "no"]:
            print("Cancelled.")
            return None
        elif confirm in ["y", "yes"]:
            break
        else:
            print("Please enter either [Y] or [N], without brackets.")

    # Data driven edit loop
    print(f"\n--- EDIT MODE (Press 'Enter' to keep current value) ---")

    # We initialize our payload with the OLD values.
    # If the user skips everything, we just send the old data back (safe).

    updated_payload = {
        "date": current_data["date"],
        "time": current_data["time"],
        "exercise": current_data["exercise"],
        "duration": current_data["duration"],
        "calories": current_data["calories"],
    }

    # Config: (Key in Dictionary, Display Name, Data Type)

    edit_config = [
        ("exercise", "Exercise Name", str),
        ("duration", "Duration (min)", int),
        ("calories", "Calories (cal)", int),
    ]

    for key, label, data_type in edit_config:
        # Get the old value to show to the user
        old_val = updated_payload[key]

        while True:
            user_input = input(f"{label} {old_val}: ").strip()

            # User hit ENTER -> Keep the old value
            if user_input == "":
                print(f"Keeping: {old_val}")
                break

            # User typed something -> VALIDATE
            if data_type == int:
                try:
                    new_val = int(user_input)
                    updated_payload[key] = new_val
                    break
                except ValueError:
                    print(f"Invalid input. Please enter a number for {label}")

            elif data_type == str:
                updated_payload[key] = user_input
                break

    final_json = {
        root_key : updated_payload
    }

    print("\nUpdating Sheet...")
    put_url = f"{SHEETY_GET}/{sheety_row_id}"

    response = requests.put(url=put_url, json=final_json, headers=sheety_headers)

    if response.status_code == 200:
        print("Success! Row updated.")
    else:
        print(f"Error: {response.text}")

    return response

def delete_activity():
    # Show all the table
    all_table, table_response, table_len = get_table("all")
    print(all_table)

    while True:
        try:
            what_row = int(input("\nWhat row do you want to delete? "))
            if what_row in range(table_len):
                break # Valid number, exit loop
            else:
                print(f"Please input a number between 0 and {table_len-1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Calculate sheety ID
    sheety_row_id =all_table.iloc[what_row]["id"]

    # Show preview of the row
    only_row, _, _ = get_table(f"{sheety_row_id}")
    print(f"Expected row to delete\n{only_row}")

    # Ask what action to take
    while True:
        confirm = input(f"\n---\nRow {what_row} (id: {sheety_row_id}) will be deleted\n"
                        "Do you confirm?\n[Y][N]: ").lower().strip()

        if confirm in ["n", "no"]:
            print("\nOperation Cancelled. Nothing will be deleted")
            return None #Exit the function entirely

        elif confirm in ["y", "yes"]:
            delete_url = f"{SHEETY_GET}/{sheety_row_id}"
            response = requests.delete(url=delete_url, headers=sheety_headers)

            if response.status_code == 204:
                print("\nRow deleted successfully!")
                return None
            elif response.status_code == 200:
                print("\nRow deleted successfully!")
                return None
            else:
                print(f"Error deleting row: {response.status_code}")
                print(response.text)
                return response

        else:
            print("Please enter either [Y] or [N], without brackets.")