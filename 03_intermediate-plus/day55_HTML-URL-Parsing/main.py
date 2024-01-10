from flask import Flask
from random import randint

app = Flask(__name__)
RANDOM_NUMBER = randint(0, 9)


@app.route("/")
def welcome_page():
    """INDEX PAGE - WELCOME PAGE"""

    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route("/<int:number>")
def is_guessed(number: int):
    """IS NUMBER GUESSED?"""
    html_body = ""
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    if number < RANDOM_NUMBER:
        html_body += f"<h1 style='color: rgb({color[0]} {color[1]} {color[2]})'>Too low, try again</h1>"
        html_body += "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > RANDOM_NUMBER:
        html_body += f"<h1 style='color: rgb({color[0]} {color[1]} {color[2]})'>Too high, try again</h1>"
        html_body += "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        html_body += f"<h1 style='color: green'>You found me!</h1>"
        html_body += "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

    return html_body


if __name__ == '__main__':
    app.run(debug=True)
