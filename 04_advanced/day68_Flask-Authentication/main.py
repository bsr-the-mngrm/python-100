from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from dotenv import load_dotenv
from os import getenv

UPLOAD_FOLDER = 'static/files'
load_dotenv()

# FLASK APPLICATION SETUP
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('FLASK_APP_SECRET_KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# FLASK-LOGIN MANAGER SETUP
login_manager = LoginManager()
login_manager.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# DATABASE SETUP
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


# FLASK APPLICATION ROUTES
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        new_user = User(
            name=request.form.get('name'),
            email=request.form.get('email'),
            password=generate_password_hash(request.form.get('password'), method='pbkdf2', salt_length=8)
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for('secrets', user_id=new_user.id))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        user: User = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar()

        if check_password_hash(user.password, request.form.get('password')):
            login_user(user)

            return redirect(url_for('secrets', user_id=user.id))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    user = db.get_or_404(User, request.args.get('user_id'))

    return render_template("secrets.html", username=user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
