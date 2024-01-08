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


if __name__ == '__main__':
    pass
