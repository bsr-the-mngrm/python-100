from datetime import datetime
from random import randint
import pandas


def read_birthdays():
    return pandas.read_csv(".data/birthdays.csv").to_dict(orient="records")


def generate_birthday_message(name: str):
    n = randint(1, 3)
    with open(f".data/letter_templates/letter_{n}.txt") as letter:
        return "".join(letter.readlines()).replace("[NAME]", name)


if __name__ == '__main__':
    birthdays = read_birthdays()
    today = datetime.now()

    for birthday in birthdays:
        if birthday['month'] == today.month and birthday['day'] == today.day:
            msg = generate_birthday_message(birthday['name'])
