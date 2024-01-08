import requests
from os import getenv
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
GOOGLE_FORM_ID = getenv('GOOGLE_FORM_ID')
GOOGLE_SHEETS_ID = getenv('GOOGLE_SHEETS_ID')
GOOGLE_FORM_URL = f'https://docs.google.com/forms/d/e/{GOOGLE_FORM_ID}/viewform'
GOOGLE_SHEETS_URL = f'https://docs.google.com/spreadsheets/d/{GOOGLE_SHEETS_ID}'
DATA_SOURCE_URL = 'https://appbrewery.github.io/Zillow-Clone/'


def get_data() -> list[list]:
    f"""Returns a list of apartments with details (link, price, address)\n 
        Webscrape '{DATA_SOURCE_URL}'
        and clean the data"""

    apartment_list = []
    for apartment in zillow_soup.select('ul[class="List-c11n-8-84-3-photo-cards"] li'):
        address = apartment.select_one('address')
        if address is not None:
            apartment_details = []
            link = apartment.select_one('a[data-test="property-card-link"]')
            apartment_details.append(link.get('href'))

            price = apartment.select_one('span[data-test="property-card-price"]')
            price = price.getText().split('/')[0]
            if '+' in price:
                price = price.split('+')[0]
            apartment_details.append(price)

            address = address.getText().strip()
            if " | " in address:
                address = address.split(' | ')[1]
            apartment_details.append(address)

            apartment_list.append(apartment_details)

    return apartment_list


def fill_out_form(apartment_list: list[list]):
    """Fill out Google Form"""

    # OPEN GOOGLE FORM
    driver.get(GOOGLE_FORM_URL)

    # GO THROUGH THE APARTMENT LIST AND FILL IN THE QUESTIONS (input_element) WITH ANSWERS (apartment.pop())
    apartment_list_length = len(apartment_list)
    for _ in range(apartment_list_length):
        apartment = apartment_list.pop()
        sleep(1.5)
        for input_element in driver.find_elements(By.CSS_SELECTOR, 'input:not(input[type="hidden"]'):
            input_element.send_keys(apartment.pop())

        # GET WEBSITE LANGUAGE
        language = driver.find_element(By.XPATH, "//html").get_attribute('lang')

        if 'hu' in language:
            submit_txt = 'Küldés'
            submit_another_answer_txt = 'Másik válasz küldése'
        else:
            submit_txt = 'Submit'
            submit_another_answer_txt = 'Submit another response'

        # SUBMIT
        driver.find_element(By.XPATH, f"//span[text()='{submit_txt}']").click()
        sleep(1)

        # SUBMIT ANOTHER ANSWER
        driver.find_element(By.XPATH, f"//a[text()='{submit_another_answer_txt}']").click()


def open_spreadsheet():
    """OPEN A SPREADSHEET"""

    # OPEN GOOGLE SHEETS
    driver.get(GOOGLE_SHEETS_URL)


if __name__ == '__main__':
    # INITIALIZATION OF BEAUTIFUL SOUP
    zillow_response = requests.get(DATA_SOURCE_URL)
    zillow_soup = BeautifulSoup(zillow_response.text, 'html.parser')

    # GET DATA - WEBSCRAPE
    apartments = get_data()

    # CHECK DATA
    # pprint(apartments)

    # INITIALIZATION OF SELENIUM WEBDRIVER
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_options)

    # FILL UP GOOGLE FORM
    fill_out_form(apartments)

    # OPEN GOOGLE SHEETS
    open_spreadsheet()
