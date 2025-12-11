import requests

from config import (
    SHEETY_BEARER_KEY,
    SHEETY_GET,
    SHEET_POST,
    SHEET_PUT
)

class DataManager:
    """Handles all the read/write operations to the Google Sheet via Sheety"""
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_url = SHEETY_GET
        self.post_url = SHEET_POST
        self.put_url = SHEET_PUT
        self.headers = {"Authorization": SHEETY_BEARER_KEY,}

    def get_table(self):
        """Return all rows as list of dict [{},{}] and the worksheet name"""
        response = requests.get(url=self.get_url, headers=self.headers)
        response.raise_for_status()

        get_data = response.json()
        worksheet_name = list(get_data.keys())[0]

        get_rows = get_data[f"{worksheet_name}"]

        return get_rows, worksheet_name

    @staticmethod
    def get_schema(rows):
        """Returns the schema of the Google Sheet"""
        first_row = rows[0]

        return list(first_row.keys())

    def update_row(self, row_id: int, updates: dict):
        """
        Update a single row identified by `row_id` with the given fields in `updates`.
        Only keys in `updates` are changed.
        """
        # Build the URL for that row
        row_url = f"{self.put_url}/{row_id}"

        # Get the row from Google Sheet
        rows, worksheet_name = self.get_table()

        # Select the row
        row = next(r for r in rows if r["id"] == row_id)

        # Eliminate the "id" key,value
        del row["id"]

        # Edit only the value with the same key in the row
        for key, value in updates.items():
            if key in row:
                row[key] = value
            else:
                raise KeyError(f"Column '{key}' doesn't exist in sheet")

        # Create the payload to send to Sheety
        payload = {
            worksheet_name: row,
        }

        # Put the update
        update_response = requests.put(url=row_url, json=payload, headers=self.headers)
        update_response.raise_for_status()

        return update_response

    def add_row(self, row_data: dict):
        """
        Create a new row using the existing sheet schema.
        Missing fields are filled with empty strings, 'id' is left for Sheety to assign.
        """
        # Get worksheet name
        rows, worksheet_name = self.get_table()
        # Get the schema
        schema = self.get_schema(rows)

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