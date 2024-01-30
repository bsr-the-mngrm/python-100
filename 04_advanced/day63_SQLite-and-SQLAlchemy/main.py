from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# CREATE FLASK APP
app = Flask(__name__)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # READ ALL RECORDS
    result = db.session.execute(db.select(Book))
    all_books = result.scalars()

    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # CREATE A RECORD
        new_book = Book(title=request.form['name'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    book_id = request.args.get('id')
    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

    if request.method == 'POST':
        # UPDATE A RECORD
        book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit_rating.html', book=book)


@app.route("/delete")
def delete():
    # DELETE A RECORD
    book_id = request.args.get('id')
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
