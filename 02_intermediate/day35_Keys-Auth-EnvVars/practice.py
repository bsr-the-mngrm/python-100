from dotenv import load_dotenv
import os
import requests

load_dotenv()
weather_api_key = os.getenv('WEATHER_API_KEY')
my_lat = os.getenv('MY_LAT')
my_lng = os.getenv('MY_LNG')
parameters = {
    "appid": weather_api_key,
    "lat": my_lat,
    "lon": my_lng,
    "cnt": 4,
    "units": "metric"
}

data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)

need_umbrella = "You don't need umbrella."

for i in range(parameters['cnt']):
    if data.json()['list'][i]['weather'][0]['id'] < 700:
        need_umbrella = "Bring an umbrella."
        break

print(need_umbrella)
