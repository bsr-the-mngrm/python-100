from dotenv import load_dotenv
from twilio.rest import Client
import os
import requests

load_dotenv()

weather_api_key = os.getenv('WEATHER_API_KEY')
my_lat = os.getenv('MY_LAT')
my_lng = os.getenv('MY_LNG')

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_phone_number = os.getenv('FROM_PHONE_NUMBER')
to_phone_number = os.getenv('TO_PHONE_NUMBER')

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
        client = Client(account_sid, auth_token)
        message = client.messages\
            .create(
                body="It's gonna rain! Bring an umbrella!",
                from_=from_phone_number,
                to=to_phone_number
            )

        print(message.status)
        break
