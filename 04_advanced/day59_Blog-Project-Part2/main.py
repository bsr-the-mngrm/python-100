from flask import Flask, render_template
import requests

all_posts = requests.get('https://api.npoint.io/9e168a049320703f5f31').json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<post_id>')
def post_page(post_id):
    return render_template('post.html', post=all_posts[int(post_id)-1])


if __name__ == "__main__":
    app.run(debug=True)