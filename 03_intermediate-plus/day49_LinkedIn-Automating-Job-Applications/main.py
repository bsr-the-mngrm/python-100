import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

load_dotenv()
LINKEDIN_JOBS_URL = os.getenv('LINKEDIN_JOBS_URL')
USERNAME = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('EMAIL_PASSWORD')


def login():
    """Login to LinkedIn"""
    driver.get('https://www.linkedin.com')
    username_input = driver.find_element(By.ID, 'session_key')
    username_input.send_keys(USERNAME)

    password_input = driver.find_element(By.ID, 'session_password')
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.ENTER)


def save_job():
    time.sleep(2)
    save_button = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
    save_button.click()


if __name__ == '__main__':
    # SELENIUM INITIALIZATION
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    # LOGIN TO LINKEDIN
    login()
    driver.get(LINKEDIN_JOBS_URL)

    # SAVE JOB
    save_job()
