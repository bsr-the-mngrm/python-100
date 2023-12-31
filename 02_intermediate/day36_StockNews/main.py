import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

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
    stock_data = requests.get(url=stock_url, params=stock_url_parameters).json()['Time Series (Daily)']

    stock_data_days = [key for (key, value) in stock_data.items()][:2]
    last_day = stock_data_days[0]
    day_before = stock_data_days[1]

    stock_daily_values = [value for (key, value) in stock_data.items()][:2]
    stock_last_day_close = float(stock_daily_values[0]['4. close'])
    stock_day_before_close = float(stock_daily_values[1]['4. close'])
    stock_diff_percent = round(((stock_last_day_close - stock_day_before_close) / stock_last_day_close) * 100, 2)

    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    if abs(stock_diff_percent) >= 5:
        news_apikey = os.getenv('NEWS_API_KEY')
        news_url = 'https://newsapi.org/v2/everything'
        news_url_parameters = {
            "q": COMPANY_NAME,
            "from": day_before,
            "to": last_day,
            "sortBy": "popularity",
            "apiKey": news_apikey
        }
        news_data = requests.get(url=news_url, params=news_url_parameters).json()
        articles = news_data['articles'][:3]

        for article in articles:
            if stock_diff_percent > 0:
                stock_diff_text = f"{STOCK}: 🔺{stock_diff_percent}%\n"
            else:
                stock_diff_text = f"{STOCK}: 🔻{stock_diff_percent}%\n"
            msg = (f"{stock_diff_text}"
                   f"Headline: {article['title']}\n"
                   f"Brief: {article['description']}\n"
                   f"Source: {article['source']['name']}")

            # STEP 3: Use https://www.twilio.com
            # Send a separate message with the percentage change
            # and each article's title and description to your phone number.
            account_sid = os.getenv('TWILIO_ACCOUNT_SID')
            auth_token = os.getenv('TWILIO_AUTH_TOKEN')
            from_phone_number = os.getenv('FROM_PHONE_NUMBER')
            to_phone_number = os.getenv('TO_PHONE_NUMBER')

            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                    body=msg,
                    from_=from_phone_number,
                    to=to_phone_number
                )

            print(message.status)

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
