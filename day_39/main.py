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
        update_iatacode = data_manager.update_row(row_id=row["id"], updates={"iataCode": row["iataCode"]})


    best_deal = flight_search.find_deals(
        origin_code=departure_city_code,
        destination_code=row["iataCode"],
        max_price=float(row["lowestPrice"])
    )

    send_message = notifier.send_notification(content=best_deal)

    print(send_message.sid)

# for each row of the table
#   first check the table with destinations.
#       if there is no value then update row with the code
# use the code to check the best flight deal
#   if anyting good, send a notification,
#   else skip
