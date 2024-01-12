from flask import Flask, render_template
from random import randint
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(0, 9)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, current_year=current_year)


if __name__ == '__main__':
    app.run(debug=True)
