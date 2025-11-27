import requests
from twilio.rest import Client
import os

# latlong.net to retrive the coordinates of a city
# Milan
lat = 45.464139
long= 9.189249

# OpenWeatherMap
# link to the plans https://openweathermap.org/full-price#current
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

api_key = os.getenv("OWM_API_KEY")
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 45.464139,
    "lon": 9.189249,
    "appid": api_key,
    "cnt": 4,
}

# Twilio Account
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

# Create request to API
response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()
# print(response.json())

# Get the url that will be used for API calls
# print(response.url)

weather_data_forecast = weather_data["list"]

# Simplest version without list as asked by Angela
bring_umbrella = False
for forecast in weather_data_forecast:
    if forecast["weather"][0]["id"] < 700:
        bring_umbrella = True
        break

if bring_umbrella:
    print("Bring the umbrella")
else:
    print("You are good to go")

# Version with list of the next hours
fetch_forecast = [
    forecast["weather"][0]["id"]
    for forecast in weather_data_forecast
]

if any(code < 700 for code in fetch_forecast):
    print("Bring the umbrella")
else:
    print("You are good to go")

# print(weather_data["list"][0]["weather"][0]["id"])

# 👩🏻‍🏫Angela's solution
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+393211234567",
        to="+393211234567"
    )
    # print("Bring the umbrella")
    print(message.status) # Check if message was sent correctly
else:
    print("You are good to go")

