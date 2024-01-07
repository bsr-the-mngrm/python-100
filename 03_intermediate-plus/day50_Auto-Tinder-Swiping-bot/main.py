from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep
from os import getenv

load_dotenv()
EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')
TINDER_UID = getenv('TINDER_UID')
FB_UID = getenv('FB_UID')


def tinder_login():
    """Login to Tinder"""
    sleep(1)
    # Accept cookies
    accept_cookies_button_xpath = f'//*[@id="u-{TINDER_UID}"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]'
    accept_cookies_button = driver.find_element(By.XPATH, accept_cookies_button_xpath)
    accept_cookies_button.click()

    # Click on login button
    login_button_xpath = (f'//*[@id="u-{TINDER_UID}"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/'
                          'div[2]/a/div[2]/div[2]')
    login_button = driver.find_element(By.XPATH, login_button_xpath)
    login_button.click()

    # Choose 'Log in with Facebook' option
    facebook_login()

    print('Successful login!')


def facebook_login():
    """Facebook login management"""
    sleep(1)
    # Click on 'Log in with Facebook' option
    fb_login_button_xpath = (f'//*[@id="{FB_UID}"]/main/div/div/div[1]/div/div/div[2]/div[2]'
                             '/span/div[2]/button/div[2]/div[2]/div')
    fb_login_button = driver.find_element(By.XPATH, fb_login_button_xpath)
    fb_login_button.click()

    # Switch to Facebook login pop up window
    fb_login_page = driver.window_handles[1]
    driver.switch_to.window(fb_login_page)
    print(f"Current window: {driver.title}")

    # Accept Facebook cookies
    sleep(3)
    fb_accept_cookies_button = driver.find_element(By.CSS_SELECTOR, 'button[title^="Allow all cookies"]')
    fb_accept_cookies_button.click()

    # Add credentials
    sleep(0.5)
    fb_username_input = driver.find_element(By.ID, 'email')
    fb_password_input = driver.find_element(By.ID, 'pass')
    fb_username_input.send_keys(EMAIL)
    fb_password_input.send_keys(PASSWORD, Keys.ENTER)

    # MANUAL STEP
    input("!WARNING! - User-action needed!\n"
          "MFA is ready? [Press 'Enter']")

    # Switch back to Tinder
    driver.switch_to.window(driver.window_handles[0])
    print(f"Current window: {driver.title}")


def dismiss_all_requests():
    """Dismiss Tinder requests"""
    sleep(5)

    # Allow location
    allow_location_button_xpath = f'//*[@id="{FB_UID}"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]'
    allow_location_button = driver.find_element(By.XPATH, allow_location_button_xpath)
    allow_location_button.click()

    sleep(0.5)
    # Disallow notifications
    # notifications_button_xpath = '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]'
    # notifications_button = driver.find_element(By.XPATH, notifications_button_xpath)
    notifications_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Not interested"]')
    notifications_button.click()


def tinder_swiping():
    """Swiping logic"""

    # SET SWIPE BUTTONS' XPATH
    left_swipe_button_xpath = (f'//*[@id="u-{TINDER_UID}"]/div/div[1]/div/main/div[1]/div/div/div[1]'
                               '/div[1]/div/div[3]/div/div[2]/button')
    right_swipe_button_xpath = (f'//*[@id="u-{TINDER_UID}"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]'
                                '/div/div[3]/div/div[4]/button')
    swipe_button_xpath = right_swipe_button_xpath

    # SET SWIPE BUTTON
    swipe_button = driver.find_element(By.XPATH, swipe_button_xpath)

    # SET SWIPE COUNTS
    swipe_count = 5
    swipe_miss_count = 0

    # SWIPING
    for _ in range(swipe_count):
        try:
            swipe_button.click()

        # Catches the cases where the 'Like' / 'Dislike' button has not loaded yet, so wait 2 seconds before retrying
        except NoSuchElementException:
            sleep(5)
            swipe_miss_count += 1

        # Catches the cases where there is a 'Matched' pop-up in front of the 'Like' / 'Dislike' button
        except ElementClickInterceptedException:
            sleep(3)
            back_to_tinder_button = driver.find_element(By.LINK_TEXT, 'BACK TO TINDER')
            back_to_tinder_button.click()
            swipe_miss_count += 1
            sleep(2)

        # Add a second delay between swipes
        else:
            sleep(1)


if __name__ == '__main__':
    # INITIALIZATION OF SELENIUM WEBDRIVER
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://tinder.com')

    # LOGIN TO TINDER
    tinder_login()

    # DISMISS ALL REQUESTS
    dismiss_all_requests()

    # SWIPING
    tinder_swiping()
