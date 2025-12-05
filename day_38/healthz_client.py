import requests
from config import (
    X_APP_KEY,
    X_APP_ID,
    X_APP_POST,
)

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
