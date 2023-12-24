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
    "lon": my_lng
}

data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)

print(data.json())
