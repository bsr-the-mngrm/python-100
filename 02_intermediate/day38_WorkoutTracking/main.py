import os
import requests
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
NL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADER = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
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

    response = requests.post(url=NL_ENDPOINT, headers=HEADER, json=nl_params)

    print(response.json())


if __name__ == '__main__':
    user_input = input("Exercise: ")

    get_exercise_stats(user_input)
