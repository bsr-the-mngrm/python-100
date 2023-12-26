import requests
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('USER')
token = os.getenv('TOKEN')
pixela_endpoint = "https://pixe.la/v1/users"


def create_account():
    user_parameters = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=pixela_endpoint, json=user_parameters)
    print(response.text)


if __name__ == '__main__':
    create_account()
