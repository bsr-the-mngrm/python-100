import os
import requests
from dotenv import load_dotenv


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self.kiwi_apikey = os.getenv('KIWI_APIKEY')
        self.location_query_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.kiwi_header = {
            "apikey": self.kiwi_apikey,
            "accept": "application/json"
        }

    def get_iata_code(self, city: str) -> str:
        location_query = {
            "term": city
        }

        response = requests.get(url=self.location_query_endpoint, params=location_query, headers=self.kiwi_header)

        return response.json()['locations'][0]['code']
