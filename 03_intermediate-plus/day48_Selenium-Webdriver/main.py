from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# CONSTANTS
GAME_TIME_IN_MIN = 5
PURCHASE_WAIT_IN_SEC = 5

if __name__ == '__main__':
    # SELENIUM INITIALIZATION
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://orteil.dashnet.org/experiments/cookie/")

    # TIME VARIABLES
    current_time = time.time()
    game_over_time = current_time + GAME_TIME_IN_MIN*60
    store_checker_time = current_time
    print(f"{round(game_over_time - current_time)} seconds left.")

    # AUTO CLICKER BOT WITH DECISION-MAKING
    while game_over_time - current_time > 0:
        if current_time - store_checker_time >= PURCHASE_WAIT_IN_SEC:
            store = driver.find_elements(By.CSS_SELECTOR, "#store b")[::-1][1:]

            for upgrade_element in store:
                current_cookies_element = driver.find_element(By.ID, 'money').text
                if "," in current_cookies_element:
                    current_cookies_element = current_cookies_element.replace(",", "")
                current_cookies = int(current_cookies_element)

                upgrade_price = int("".join(upgrade_element.text.split(" - ")[1].split(',')))
                if upgrade_price < current_cookies:
                    upgrade_element.click()
                    break

            print(f"{round(game_over_time - current_time)} seconds left.")
            store_checker_time = time.time()

        current_time = time.time()
        cookie_btn = driver.find_element(By.ID, 'cookie')
        cookie_btn.click()

    # GAME OVER
    cps_text = driver.find_element(By.ID, 'cps').text.capitalize()
    cps = float(cps_text.split(" : ")[1])
    print(f"All cookies: {int(cps*300)}\n{cps_text}")

    driver.quit()
