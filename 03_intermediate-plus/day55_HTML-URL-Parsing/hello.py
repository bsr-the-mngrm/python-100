from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a paragraph</p>"
            "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzNibHhheHpqMGw1ZmNhNnl0M2xnNWpj"
            "ZWJ5YzVmM3VrZzQyd3o1MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Cm9wKmKMUlRPvdoHgU/giphy.gif'>")


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
