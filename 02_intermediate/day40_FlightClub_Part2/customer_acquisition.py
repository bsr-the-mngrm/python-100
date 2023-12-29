import os
import requests
from dotenv import load_dotenv

load_dotenv()
SHEETY_USERS_URL = os.getenv('SHEETY_USERS_URL')
SHEETY_HEADER = {
    "Authorization": f"Basic {os.getenv('SHEETY_TOKEN')}",
    "Username": os.getenv('USER'),
    "Password": os.getenv('PASSWORD')
}

new_user = {
    "user": {
        "firstName": input("What's your first name?\n"),
        "lastName": input("What's your last name?\n"),
        "email": input("What's your email?\n")
    }
}

response = requests.post(url=SHEETY_USERS_URL, headers=SHEETY_HEADER, json=new_user)

print(response.text)
