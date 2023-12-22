from datetime import datetime
from random import choice


def read_quotes():
    with (open("data/quotes.txt", mode='r') as quotes_file):
        qs = []
        for row in quotes_file.readlines():
            qs.append(row.strip())
    return qs


if __name__ == '__main__':
    quotes = read_quotes()
    day_of_week = datetime.now().weekday()

    if day_of_week == 4:
        chosen_quote = choice(quotes)
