from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# Different routes using the app.route decorator
@app.route("/bye")
def say_bye():
    return "<h1>Bye!</h1>"


# Creating variable paths and converting the path to a specified data type
@app.route("/<name>")
def greet(name):
    return f"Hello there {name}!"


if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
