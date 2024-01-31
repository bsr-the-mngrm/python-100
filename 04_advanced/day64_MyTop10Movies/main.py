from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# CREATE FLASK APP
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('FLASK_APP_SECRET_KEY')
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    __tablename__ = 'movie'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# CREATE TABLE SCHEMA IN THE DATABASE
with app.app_context():
    db.create_all()


# MOVIE WTFORM
class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


@app.route("/")
def home():
    my_top_movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars().all()

    return render_template("index.html", movies=my_top_movies)


@app.route("/add")
def add():
    pass


@app.route("/update", methods=['GET', 'POST'])
def update():
    movie_id = request.args.get('id')
    movie_to_update = db.get_or_404(Movie, movie_id)
    form = RateMovieForm()

    if form.validate_on_submit():
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit.html', form=form, movie=movie_to_update)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    # # After adding the new_movie the code needs to be commented out/deleted.
    # # So you are not trying to add the same movie twice. The db will reject non-unique movie titles.
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
    #                 "extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's "
    #                 "negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # second_movie = Movie(
    #     title="Avatar The Way of Water",
    #     year=2022,
    #     description="Set more than a decade after the events of the first film, learn the story of the Sully family "
    #                 "(Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep "
    #                 "each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #     rating=7.3,
    #     ranking=9,
    #     review="I liked the water.",
    #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    # )
    #
    # # CREATE TABLE SCHEMA IN THE DATABASE
    # with app.app_context():
    #     db.create_all()
    #     db.session.add_all([new_movie, second_movie])
    #     db.session.commit()
    #
    # app.run()

    app.run(debug=True)
