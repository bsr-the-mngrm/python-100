from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = randint(0, 9)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, current_year=current_year)


@app.route('/guess/<name>')
def guess(name):
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()['gender']
    age = requests.get(f"https://api.agify.io/?name={name}").json()['age']

    return render_template('guess.html', name=name, gender=gender, age=age)


@app.route('/blog')
def blog_home_page():
    all_posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
