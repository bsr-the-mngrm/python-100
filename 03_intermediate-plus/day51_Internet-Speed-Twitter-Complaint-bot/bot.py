from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class InternetSpeedTwitterBot:
    def __init__(self, up: int, down: int, isp_twitter_username: str):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        self.up = up
        self.down = down
        self.driver = webdriver.Chrome(options=chrome_options)
        self.isp_twitter_username = isp_twitter_username

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        sleep(3)
        self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        self.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="start speed test - connection type multi"]').click()
        sleep(40)
        up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text

        return {"up": up, "down": down}

    def tweet_at_provider(self):
        pass
