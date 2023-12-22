from datetime import datetime
from random import randint
from dotenv import load_dotenv
import pandas
import os
import smtplib


def read_birthdays():
    return pandas.read_csv(".data/birthdays.csv").to_dict(orient="records")


def generate_birthday_message(name: str):
    n = randint(1, 3)
    with open(f".data/letter_templates/letter_{n}.txt") as letter:
        return "".join(letter.readlines()).replace("[NAME]", name)


def send_birthday_wish(birthday_msg):
    load_dotenv('env/.env')

    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_APP_KEY')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as connection:
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f"Subject:Happy Birthday!\n\n"
                f"{birthday_msg}"
        )


if __name__ == '__main__':
    birthdays = read_birthdays()
    today = datetime.now()

    for birthday in birthdays:
        if birthday['month'] == today.month and birthday['day'] == today.day:
            msg = generate_birthday_message(birthday['name'])
            send_birthday_wish(msg)
