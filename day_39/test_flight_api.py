import requests

from config import AMADEUS_URL_CHEAPEST_DATE
import pandas as pd

from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager

amadeus = FlightSearch()
data_manager = DataManager()
notifier = NotificationManager()

# # --- AMADEUS API TEST ---
# # Get the first request
#
# get_url = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
#
# # get_url = AMADEUS_URL_CHEAPEST_DATE
# amadeus_token = amadeus.get_token()
#
# amadeus_headers = {
#     "Authorization": f"Bearer {amadeus_token}",
# }
#
# amadeus_params = {
#     "origin": "MIL",
#     "destination": "PAR",
#     "maxPrice": 20,
# }
#
# response = requests.get(url=get_url, params=amadeus_params, headers=amadeus_headers)
#
# get_search_response = response.json()
#
# print(get_search_response)
#
# # ---
#
# # --- AMADEUS FIND CHEAPEST DATE ---
#
# find_deals = amadeus.find_deals(origin_code="MIL", destination_code="PAR",  max_price=300)
# # find_deals.raise_for_status()
#
# print(find_deals)
#
# data = find_deals.json()["data"]
#
# rows = [
#     {
#         "origin": item["origin"],
#         "destination": item["destination"],
#         "departure": item["departureDate"],
#         "price": float(item["price"]["total"]),
#     }
#     for item in data
# ]
#
# df = pd.DataFrame(rows).sort_values("price")
#
# print(df.to_string(index=False))
#
# # ---

# # --- TRY CITY IATA CODE ---
#
# iata_code = amadeus.get_iata_code(city_name="Barcelona")
# print(iata_code)
#
# # ---

# # --- Twilio test --
# data = FlightData(price=200, departure_code="MIL", arrival_code="BCN", departure_date="2025-12-24", start_date="2025-12-10", end_date="2025-04-29")
#
# message = NotificationManager()
#
# send_messsage = message.send_notification(data)
#
# print(send_messsage)
# # ---

# --- Sheety testing ---

rows, _ = data_manager.get_table()


update_response = data_manager.update_row(row_id=2, updates={"iataCode": "MIL"})

print(update_response.status_code)
# ---