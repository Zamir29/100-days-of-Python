from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notifier = NotificationManager()

departure_city_code = "MIL" # This can be an input request from the user

# Get the row from the table on Google Sheet
rows, _ = data_manager.get_table()

# For each row check if there is any field empty to fill.
for row in rows:
    if not row["iataCode"]:
        row["iataCode"] = flight_search.get_iata_code(city_name=row["city"])
        data_manager.update_row(row_id=row["id"], updates={"iataCode": row["iataCode"]})

    try:
        best_deal = flight_search.find_deals(
            origin_code=departure_city_code,
            destination_code=row["iataCode"],
            max_price=float(row["lowestPrice"])
        )

        message_id = notifier.send_notification(content=best_deal)

        print(f"Alert send for {row['city']} - Twilio SID: {message_id}")

    except ValueError as error_message:
        # The ValueError in each step of any method will be printed and will interrupt this instance
        print(f"Skipping destination from {departure_city_code} to {row['iataCode']}: {error_message}")
        continue

# for each row of the table
#   first check the table with destinations.
#       if there is no value then update row with the code
# use the code to check the best flight deal
#   if anything good, send a notification,
#   else skip
