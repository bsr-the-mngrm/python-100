from bot import InternetSpeedTwitterBot
from dotenv import load_dotenv
from os import getenv

load_dotenv()
PROMISED_DOWN = 900
PROMISED_UP = 300
TWITTER_EMAIL = getenv('TWITTER_EMAIL')
TWITTER_USERNAME = getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = getenv('TWITTER_PASSWORD')
ISP_TWITTER_USERNAME = getenv('ISP_TWITTER_USERNAME')


if __name__ == '__main__':
    # INITIALIZE BOT
    my_bot = InternetSpeedTwitterBot(PROMISED_UP, PROMISED_DOWN, ISP_TWITTER_USERNAME)

    # GET INTERNET SPEED VALUES
    result = my_bot.get_internet_speed()

    # SEND A TWEET TO ISP IF RESULTS ARE LOWER THAN THE PROMISED ONES
    if result['down'] < PROMISED_DOWN or result['up'] < PROMISED_UP:
        tweet = (f"Dear @{ISP_TWITTER_USERNAME}, my internet speed is {result['down']}down/{result['up']}up.\n"
                 f"(promised values: DOWN - {PROMISED_DOWN} Mbps / UP - {PROMISED_UP} Mbps)")
        my_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_USERNAME, TWITTER_PASSWORD, tweet)
        print("Tweet sent to ISP.")
    else:
        print(f"There is no complaints.\n"
              f"My internet speed is {result['down']}down/{result['up']}up.\n"
              f"(promised values: DOWN - {PROMISED_DOWN} Mbps / UP - {PROMISED_UP} Mbps)")
