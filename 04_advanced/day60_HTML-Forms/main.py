from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        return render_template('welcome.html', username=request.form['username'], password=request.form['password'])
    else:
        return home()


if __name__ == '__main__':
    app.run(debug=True)
