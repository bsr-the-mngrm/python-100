from datetime import datetime
from random import choice
from dotenv import load_dotenv
import os
import smtplib


def read_quotes():
    with (open("data/quotes.txt", mode='r') as quotes_file):
        qs = []
        for row in quotes_file.readlines():
            qs.append(row.strip())
    return qs


def send_quote(q: str):
    load_dotenv('env/.env')

    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_APP_KEY')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f'Subject:Motivation Mail\n\n'
                f'Your message today:\n'
                f'{q}'
        )


if __name__ == '__main__':
    quotes = read_quotes()
    day_of_week = datetime.now().weekday()

    if day_of_week == 4:
        chosen_quote = choice(quotes)
        send_quote(chosen_quote)
