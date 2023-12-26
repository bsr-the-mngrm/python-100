import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv('USER')
TOKEN = os.getenv('TOKEN')
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
TODAY = datetime.now()
HEADERS = {
    "X-USER-TOKEN": TOKEN
}


def create_account():
    user_parameters = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
    print(response.text)


def create_graph():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }

    response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)
    print(response.text)


def post_pixel():
    pixel_config = {
        "date": TODAY.strftime("%Y%m%d"),
        "quantity": "4.5"
    }

    response = requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", json=pixel_config, headers=HEADERS)
    print(response.text)


if __name__ == '__main__':
    # create_account()

    # create_graph()

    post_pixel()
