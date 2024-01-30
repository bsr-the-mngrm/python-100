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
    __tablename__ = "books"

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
    # new_book = Book(id=2, title='Harry Potter2', author='J.K. Rowling', rating=9.3)
    new_book = Book(title='Harry Potter3', author='J.K. Rowling', rating=9.3)
    db.session.add(new_book)
    db.session.commit()


# Read all records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books.all())


# Read a particular record by query
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    print(book)


# Update a particular record by query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter2")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()


# Update a record by primary key
book_id = 3
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# Delete a particular record by primary key
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
