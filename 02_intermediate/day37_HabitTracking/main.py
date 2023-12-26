import requests
import os
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv('USER')
TOKEN = os.getenv('TOKEN')
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"


def create_account():
    user_parameters = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
    print(response.text)


if __name__ == '__main__':
    create_account()
