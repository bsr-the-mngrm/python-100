from bot import InternetSpeedTwitterBot
from dotenv import load_dotenv
from os import getenv

load_dotenv()
PROMISED_DOWN = 900
PROMISED_UP = 300
TWITTER_EMAIL = getenv('TWITTER_EMAIL')
TWITTER_PASSWORD = getenv('TWITTER_PASSWORD')
ISP_TWITTER_USERNAME = getenv('ISP_TWITTER_USERNAME')


if __name__ == '__main__':
    my_bot = InternetSpeedTwitterBot(PROMISED_UP, PROMISED_DOWN, ISP_TWITTER_USERNAME)
    print(my_bot.get_internet_speed())
    my_bot.tweet_at_provider()
