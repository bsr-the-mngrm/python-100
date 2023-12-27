import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
NL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NL_HEADER = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
SHEETY_URL = os.getenv('SHEETY_URL')
SHEETY_HEADER = {
    "Authorization": f"Basic {os.getenv('SHEETY_TOKEN')}",
    "Username": os.getenv('USER'),
    "Password": os.getenv('PASSWORD')
}

GENDER = os.getenv('GENDER')
WEIGHT = os.getenv('WEIGHT')
HEIGHT = os.getenv('HEIGHT')
AGE = os.getenv('AGE')


def get_exercise_stats(exercise: str):
    nl_params = {
        "query": exercise,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE
    }

    response = requests.post(url=NL_ENDPOINT, headers=NL_HEADER, json=nl_params)

    now = datetime.now()

    return {"date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": response.json()['exercises'][0]['name'].title(),
            "duration": response.json()['exercises'][0]['duration_min'],
            "calories": response.json()['exercises'][0]['nf_calories']}


def post_to_sheets(stat):
    workout = {
        "workout": stat
    }

    response = requests.post(url=SHEETY_URL, json=workout, headers=SHEETY_HEADER)

    print(response.json())


if __name__ == '__main__':
    user_input = input("Exercise: ")
    result = get_exercise_stats(user_input)
    post_to_sheets(result)
