from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice
from dotenv import load_dotenv
from os import getenv

load_dotenv()
app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # # Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Alternatively use Dictionary Comprehension to do the same thing
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe: Cafe = choice(all_cafes)

    # # Write out all columns
    # return jsonify(cafe={
    #     # Omit the id from the response
    #     # id=random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "amenities": {
    #         "seats": random_cafe.seats,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_sockets": random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price
    #     }
    # })

    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()

    return {"cafes": [cafe.to_dict() for cafe in all_cafes]}


@app.route("/search")
def search():
    query_location = request.args.get("loc")
    if query_location:
        cafes = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()

        if not cafes:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    else:
        cafes = db.session.execute(db.select(Cafe)).scalars().all()

    return {"result": [cafe.to_dict() for cafe in cafes]}


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_new_cafe():
    new_cafe = Cafe(name=request.form["name"],
                    map_url=request.form["map_url"],
                    img_url=request.form["img_url"],
                    location=request.form["location"],
                    seats=request.form["seats"],
                    has_toilet=bool(request.form["has_toilet"]),
                    has_wifi=bool(request.form["has_wifi"]),
                    has_sockets=bool(request.form["has_sockets"]),
                    can_take_calls=bool(request.form["can_take_calls"]),
                    coffee_price=request.form["coffee_price"])

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = db.session.get(Cafe, cafe_id)

    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": f"{cafe_to_update.name} successfully updated."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api-key") == getenv('API-KEY'):
        cafe_to_delete = db.session.get(Cafe, cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": f"{cafe_to_delete.name} successfully deleted."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you haver the correct api_key."), 403


if __name__ == '__main__':
    app.run(debug=True)
