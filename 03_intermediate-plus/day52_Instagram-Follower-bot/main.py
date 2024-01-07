from bot import InstagramFollowerBot
from dotenv import load_dotenv
from os import getenv

load_dotenv()
INSTAGRAM_USERNAME = getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = getenv('INSTAGRAM_PASSWORD')
TARGET_ACCOUNT_NAME = getenv('TARGET_ACCOUNT_NAME')


if __name__ == '__main__':
    my_bot = InstagramFollowerBot()
    my_bot.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    my_bot.find_followers(TARGET_ACCOUNT_NAME)
