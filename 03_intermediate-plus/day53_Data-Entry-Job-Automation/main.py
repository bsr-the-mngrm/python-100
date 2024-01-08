from pprint import pprint

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from dotenv import load_dotenv
from os import getenv

load_dotenv()
GOOGLE_FORM_ID = getenv('GOOGLE_FORM_ID')
GOOGLE_SHEETS_ID = getenv('GOOGLE_SHEETS_ID')
GOOGLE_FORM_URL = f'https://docs.google.com/forms/d/e/{GOOGLE_FORM_ID}/viewform'
GOOGLE_SHEETS_URL = f'https://docs.google.com/spreadsheets/d/{GOOGLE_SHEETS_ID}'
DATA_SOURCE_URL = 'https://appbrewery.github.io/Zillow-Clone/'


def get_data() -> list[dict]:
    f"""Returns a list of apartments with details (address, link, price)\n 
        Webscrape '{DATA_SOURCE_URL}'
        and clean the data"""

    zillow_response = requests.get(DATA_SOURCE_URL)
    zillow_soup = BeautifulSoup(zillow_response.text, 'html.parser')

    apartment_list = []
    for apartment in zillow_soup.select('ul[class="List-c11n-8-84-3-photo-cards"] li'):
        address = apartment.select_one('address')
        if address is not None:
            address = address.getText().strip()
            if " | " in address:
                address = address.split(' | ')[1]
            apartment_dict = {'address': address}

            price = apartment.select_one('span[data-test="property-card-price"]')
            price = price.getText().split('/')[0]
            if '+' in price:
                price = price.split('+')[0]
            apartment_dict['price'] = price

            link = apartment.select_one('a[data-test="property-card-link"]')
            apartment_dict['link'] = link.get('href')

            apartment_list.append(apartment_dict)

    return apartment_list


if __name__ == '__main__':
    # GET DATA - WEBSCRAPE
    get_data()
