import requests
from flight_search import FlightSearch
import pandas

# AMADEUS API TEST
# Get the first request

amadeus = FlightSearch()

# get_url = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
#
# amadeus_token = amadeus.get_token()
#
# amadeus_headers = {
#     "Authorization": f"Bearer {amadeus_token}",
# }
#
# amadeus_params = {
#     "origin": "PAR",
#     # "destination": "CAS",
#     "maxPrice": 200,
# }
#
# response = requests.get(url=get_url, params=amadeus_params, headers=amadeus_headers)
#
# get_search_response = response.json()

find_deals = amadeus.find_deals()

print(find_deals.json())

# get_table = get_search_response["data"][:3]
#
# show_table = pandas.DataFrame.from_dict(get_table)
#
# print(show_table)

# ---
