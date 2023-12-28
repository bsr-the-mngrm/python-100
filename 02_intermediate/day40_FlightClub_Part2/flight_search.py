import os
import requests
from dotenv import load_dotenv
from flight_data import FlightData
from datetime import datetime


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self.kiwi_apikey = os.getenv('KIWI_APIKEY')
        self.kiwi_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.kiwi_location_query_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.kiwi_header = {
            "apikey": self.kiwi_apikey,
            "accept": "application/json"
        }

    def get_iata_code(self, city: str) -> str:
        location_query = {
            "term": city
        }

        response = requests.get(url=self.kiwi_location_query_endpoint,
                                headers=self.kiwi_header,
                                params=location_query)

        return response.json()['locations'][0]['code']

    def get_cheapest_flight(self, fly_from: tuple, fly_to, date_from: datetime, date_to: datetime) -> FlightData:
        flight_query = {
            "fly_from": fly_from[1],
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "adults": 1,
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "sort": "price"
        }

        response = requests.get(url=self.kiwi_search_endpoint, params=flight_query, headers=self.kiwi_header)

        try:
            cheapest_flight = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {fly_from[1]} to {fly_to}.")
            return None

        return FlightData(f"{fly_from[0]}-{fly_from[1]}",
                          f"{cheapest_flight['cityTo']}-{cheapest_flight['flyTo']}",
                          cheapest_flight["route"][0]["local_departure"].split('T')[0],
                          cheapest_flight["route"][1]["local_departure"].split('T')[0],
                          cheapest_flight['price'])
