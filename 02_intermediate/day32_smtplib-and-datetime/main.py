from datetime import datetime
import pandas


def read_birthdays():
    return pandas.read_csv(".data/birthdays.csv").to_dict(orient="records")


if __name__ == '__main__':
    birthdays = read_birthdays()
    today = datetime.now()

    for birthday in birthdays:
        if birthday['month'] == today.month and birthday['day'] == today.day:
            pass
