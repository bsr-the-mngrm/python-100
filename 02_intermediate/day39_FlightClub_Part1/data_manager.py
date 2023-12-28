import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from flight_data import FlightData
from flight_search import FlightSearch


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.sheety_url = os.getenv('SHEETY_URL')
        self.sheety_header = {
            "Authorization": f"Basic {os.getenv('SHEETY_TOKEN')}",
            "Username": os.getenv('USER'),
            "Password": os.getenv('PASSWORD')
        }
        self.flight_search = FlightSearch()

    def get_deals(self) -> list:
        deals = requests.get(url=self.sheety_url, headers=self.sheety_header).json()['prices']

        for deal in deals:
            if deal['iataCode'] == '':
                deal['iataCode'] = self.flight_search.get_iata_code(deal['city'])

        return deals

    def update_deals(self):
        pass
