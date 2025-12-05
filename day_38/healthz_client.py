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

sheety_headers = {
        "Authorization": SHEETY_BEARER_KEY,
    }

app_headers = {
    "X-APP-ID": X_APP_ID,
    "X-APP-KEY": X_APP_KEY,
}

detail_data = {
    "query": ("Tell me which exercise you did: ", str),
    "weight_kg": ("What's your weight?\nkg: ", int),
    "height_cm": ("What's your height?\ncm: ", int),
    "age": ("What's your age?\nnumber: ", int),
    "gender": ("What's your gender?\n[male][female]: ", str),

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

def get_details():
    query_params = {}

    # We create a flag to track if we have already asked the "More details" question
    asked_permission = False

    for key, (prompt, data_type) in detail_data.items():

        # --- LOGIC TO SKIP OPTIONAL QUESTIONS ---
        # If this key is NOT 'query', we need to check if the user wants to proceed
        if key != "query":

            # If we haven't asked yet, ask now!
            if not asked_permission:
                while True:
                    more_details = input("Do you want to add more details?\n[Y] [N]: ").lower().strip()
                    if more_details in ["n", "no"]:
                        return query_params # Stop here and return what we have (just the query)
                    elif more_details in ["y", "yes"]:
                        asked_permission = True # Mark as asked, so we don't ask again
                        break
                    else:
                        print("Please enter either [Y] or [N], without brackets.")

        # --- INPUT COLLECTION LOGIC ---
        while True:
            user_input = input(prompt)

            try:
                # 1. Check if the required type is an integer
                if data_type == int:
                    # This will rais ValueError if input is not a number
                    converted_value = int(user_input)
                    query_params[key] = converted_value
                    break

                # 2. Check if the required type is a string
                elif data_type == str:
                    # Manual check: We don't want empty strings
                    if len(user_input.strip()) == 0:
                        print("Input cannot be empty.")
                        continue

                    # Specific check for gender to ensure API compatibility
                    if key == "gender" and user_input.lower().strip() not in ["male", "female"]:
                        print("Please type 'male' or 'female'.")
                        continue

                    query_params[key] = user_input
                    break

            except ValueError:
                print(f"Invalid input. Please enter a valid {data_type.__name__}.")

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
    all_table, _, table_len = get_table("all")
    print(all_table)

    # Select row
    while True:
        try:
            what_row = int(input("What row do you want to edit? "))
            if what_row in range(table_len):
                break  # Valid number, exit loop
            else:
                print(f"Please input a number between 0 and {table_len - 1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Show row preview
    row_df, row_response, _ = get_table(f"{what_row}")
    print(f"\nExpected row to edit\n{row_df}")

    sheety_row_id = str(what_row + 2)
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
            what_row = int(input("What row do you want to delete? "))
            if what_row in range(table_len):
                break # Valid number, exit loop
            else:
                print(f"Please input a number between 0 and {table_len-1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Show preview of the row
    only_row, _, _ = get_table(what_row)
    print(f"Expected row to delete\n{only_row}")

    # Ask what action to take
    while True:
        confirm = input(f"\n---\nRow {what_row} will be deleted\n"
                        "Do you confirm?\n[Y][N]: ").lower().strip()

        if confirm in ["n", "no"]:
            print("\nOperation Cancelled. Nothing will be deleted")
            return None #Exit the function entirely

        elif confirm in ["y", "yes"]:
            sheety_row_id = str(what_row + 2)

            delete_url = f"{SHEETY_GET}/{sheety_row_id}"
            response = requests.delete(url=delete_url, headers=sheety_headers)

            if response.status_code == 200:
                print("\nRow deleted successfully!")
            else:
                print(f"Error deleting row: {response.text}")

            return response

        else:
            print("Please enter either [Y] or [N], without brackets.")