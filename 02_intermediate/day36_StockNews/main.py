import os
import requests
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


if __name__ == '__main__':
    load_dotenv()

    # STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    stock_apikey = os.getenv('STOCK_API_KEY')
    stock_url = 'https://www.alphavantage.co/query'
    stock_url_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": stock_apikey
    }
    stock_data = requests.get(url=stock_url, params=stock_url_parameters).json()
    stock_last_day_close = float(stock_data['Time Series (Daily)']['2023-12-22']['4. close'])
    stock_day_before_close = float(stock_data['Time Series (Daily)']['2023-12-21']['4. close'])
    stock_diff_percent = round(((stock_last_day_close - stock_day_before_close) / stock_last_day_close) * 100, 2)

    if abs(stock_diff_percent) >= 5:
        print("Get News")

    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.

    # Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
    by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, 
    near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
    by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near 
    the height of the coronavirus market crash.
    """
