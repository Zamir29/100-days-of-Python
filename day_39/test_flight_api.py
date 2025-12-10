import requests

from config import AMADEUS_URL_CHEAPEST_DATE
import pandas as pd
from flight_search import FlightSearch

amadeus = FlightSearch()

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
# --- AMADEUS FIND CHEAPEST DATE ---

find_deals = amadeus.find_deals(origin_code="MIL", destination_code="PAR",  max_price=300)
# find_deals.raise_for_status()

print(find_deals)

data = find_deals.json()["data"]

rows = [
    {
        "origin": item["origin"],
        "destination": item["destination"],
        "departure": item["departureDate"],
        "price": float(item["price"]["total"]),
    }
    for item in data
]

df = pd.DataFrame(rows).sort_values("price")

print(df.to_string(index=False))

# ---

# # --- TRY CITY IATA CODE ---
#
# iata_code = amadeus.get_iata_code(city_name="Barcelona")
# print(iata_code)

