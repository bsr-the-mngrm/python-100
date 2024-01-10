from flask import Flask
from random import randint

app = Flask(__name__)
RANDOM_NUMBER = randint(0, 9)


# INDEX PAGE - WELCOME PAGE
@app.route("/")
def welcome_page():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


if __name__ == '__main__':
    app.run(debug=True)
