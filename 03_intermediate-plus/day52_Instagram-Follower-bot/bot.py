from selenium import webdriver


class InstagramFollowerBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome()

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass
