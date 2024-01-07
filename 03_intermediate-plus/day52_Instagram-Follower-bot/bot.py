from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
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

    def find_followers(self, target_account):
        """Find the target account's followers"""
        self.driver.get(f"https://www.instagram.com/{target_account}/followers/")

        sleep(5)
        follower_list_xpath = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div'
        follower_list = self.driver.find_element(By.XPATH, follower_list_xpath).find_elements(By.TAG_NAME, 'button')

        self.__follow(follower_list)

    def __follow(self, follower_list: list[WebElement]):
        """Follow the accounts on a given list"""
        for follow_button in follower_list:
            try:
                sleep(1)
                follow_button.click()
            except ElementClickInterceptedException:
                sleep(1)
                self.driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
