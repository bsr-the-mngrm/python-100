from selenium import webdriver


class InternetSpeedTwitterBot:
    def __init__(self, up: int, down: int, isp_twitter_username: str):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        self.up = up
        self.down = down
        self.driver = webdriver.Chrome(options=chrome_options)
        self.isp_twitter_username = isp_twitter_username

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass
