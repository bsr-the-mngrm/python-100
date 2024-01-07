from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
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

    def get_internet_speed(self) -> dict:
        """Returns the internet speed (up and down values in Mbps)"""
        self.driver.get('https://www.speedtest.net')
        sleep(3)
        self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        self.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="start speed test - connection type multi"]').click()
        sleep(40)
        up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text

        return {"up": up, "down": down}

    def tweet_at_provider(self, email: str, username: str, password: str, tweet: str):
        """Login to Twitter and send tweet to ISP"""
        # LOGIN TO TWITTER
        self.driver.get('https://twitter.com/i/flow/login')
        sleep(3)
        self.driver.find_element(By.NAME, 'text').send_keys(email, Keys.ENTER)
        try:
            sleep(3)
            self.driver.find_element(By.NAME, 'password').send_keys(password, Keys.ENTER)

        # It catches if the login service needs a username also
        except NoSuchElementException:
            sleep(3)
            self.driver.find_element(By.NAME, 'text').send_keys(username, Keys.ENTER)
            sleep(3)
            self.driver.find_element(By.NAME, 'password').send_keys(password, Keys.ENTER)

        # ACCEPT COOKIES
        sleep(5)
        accept_cookies_xpath = '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div'
        self.driver.find_element(By.XPATH, accept_cookies_xpath).click()

        # SEND TWEET TO ISP
        whats_happening_xpath = ('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/'
                                 'div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/'
                                 'div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')

        whats_happening = self.driver.find_element(By.XPATH, whats_happening_xpath)
        whats_happening.send_keys(tweet)

        post_xpath = ('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div'
                      '/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div')
        self.driver.find_element(By.XPATH, post_xpath).click()
