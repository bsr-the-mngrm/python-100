from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# CREATE FLASK APP
app = Flask(__name__)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# SET DATABASE URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection-practice.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


# Create record
with app.app_context():
    new_book = Book(id=1, title='Harry Potter', author='J.K. Rowling', rating=9.3)
    db.session.add(new_book)
    db.session.commit()
