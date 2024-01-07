from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep


class InstagramFollowerBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, username: str, password: str):
        """Login to Instagram"""
        self.driver.get('https://www.instagram.com/accounts/login/')

        # ACCEPT COOKIES
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Allow all cookies']").click()

        # ADD CREDENTIALS
        sleep(1)
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password, Keys.ENTER)

        # DISMISS POP-UPs
        sleep(10)
        self.driver.find_element(By.XPATH, "//div[text()='Not now']").click()

        try:
            sleep(3)
            self.driver.find_element(By.XPATH, "//button[text()='Not Now']").click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        pass

    def follow(self):
        pass
