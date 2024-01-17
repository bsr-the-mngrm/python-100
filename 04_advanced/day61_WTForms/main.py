from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from dotenv import load_dotenv
from os import getenv
from flask_bootstrap import Bootstrap5

load_dotenv()
app = Flask(__name__)
app.secret_key = getenv('FLASK_APP_SECRET_KEY')
bootstrap = Bootstrap5(app)


class LoginForm(FlaskForm):
    email = StringField(label='Email: ', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password: ', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == getenv('ADMIN_EMAIL') and login_form.password.data == getenv('ADMIN_PASSWORD'):
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template('login.html', form=login_form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/denied')
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
