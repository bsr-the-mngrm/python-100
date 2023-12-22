import pandas


def read_birthdays():
    return pandas.read_csv(".data/birthdays.csv").to_dict(orient="records")


if __name__ == '__main__':
    birthdays = read_birthdays()
