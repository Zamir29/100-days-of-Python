import requests

from config import SHEETY_BEARER_KEY, SHEETY_GET, SHEET_POST

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_url = SHEETY_GET
        self.post_url = SHEET_POST
        self.put_url = SHEET_POST
        self.headers = {"Authorization": SHEETY_BEARER_KEY,}

    def get_table(self):

        response = requests.get(url=self.get_url, headers=self.headers)
        response.raise_for_status()

        get_data = response.json()
        worksheet_name = list(get_data.keys())[0]

        get_rows = get_data[f"{worksheet_name}"]

        return get_rows, worksheet_name

    def get_schema(self):
        rows, _ = self.get_table()
        first_row = rows[0]

        return list(first_row.keys())

    def update_row(self, row_id: int, updates: dict):
        # Build the URL for that row
        row_url = f"{self.put_url}/{row_id}"

        # Get the row from Google Sheet
        rows, worksheet_name = self.get_table()

        row = next(r for r in rows if r["id"] == row_id)

        # Edit only the value wit the same key in the row
        for key, value in updates.items():
            row[key] = value

        # Create the payload to send to Sheety
        payload = {
            worksheet_name: row,
        }

        # Put the update
        update_response = requests.put(url=row_url, json=payload, headers=self.headers)
        update_response.raise_for_status()

        return update_response

    def add_row(self, row_data: dict):
        # Get worksheet name
        _,  worksheet_name = self.get_table()
        # Get the schema
        schema = self.get_schema()

        # build the new row
        new_row = {}
        for key in schema:
            if key == "id":
                continue
            new_row[key] = row_data.get(key, "")

        payload = {
            worksheet_name: new_row,
        }

        response = requests.post(url=self.post_url, json=payload, headers=self.headers)
        response.raise_for_status()

        return response