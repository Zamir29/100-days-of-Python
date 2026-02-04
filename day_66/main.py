'''
Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


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
        """
        Use the dict comprehension to build dynamically
        a dict of column names and their attribute
        """
        return { column.name : getattr(self, column.name) for column in self.__table__.columns} # type: ignore[reportAttributeAccessIssue]


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")



# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafe_db = db.select(Cafe)
    result = db.session.execute(cafe_db)
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)

    # cafe_json = jsonify(cafe={
    #     "id": cafe.id,
    #     "name": cafe.name,
    #     "map_url": cafe.map_url,
    #     "img_url": cafe.img_url,
    #     "location": cafe.location,
    #     "seats": cafe.seats,
    #     "has_toilet": cafe.has_toilet,
    #     "has_wifi": cafe.has_wifi,
    #     "has_sockets": cafe.has_sockets,
    #     "can_take_calls": cafe.can_take_calls,
    #     "coffee_price": cafe.coffee_price,
    # })
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafe_db = db.select(Cafe)
    result = db.session.execute(cafe_db)
    all_cafes = result.scalars().all()

    # all_cafes_dict = []
    # for cafe in all_cafes:
    #     cafe_item = {
    #     "id": cafe.id,
    #     "name": cafe.name,
    #     "map_url": cafe.map_url,
    #     "img_url": cafe.img_url,
    #     "location": cafe.location,
    #     "seats": cafe.seats,
    #     "has_toilet": cafe.has_toilet,
    #     "has_wifi": cafe.has_wifi,
    #     "has_sockets": cafe.has_sockets,
    #     "can_take_calls": cafe.can_take_calls,
    #     "coffee_price": cafe.coffee_price,
    #     }
    #     all_cafes_dict.append(cafe_item)

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=["GET"])
def get_cafe_at_location():
    """Use the Flask request.args to get the parameter from the URL

    Returns:
        json: a Response with a json file list of cafes in that location otherwise a 404 error
    """
    query_location = request.args.get("loc")

    if query_location is None:
        return jsonify(error={"Bad Request": "Missing 'loc' parameter"}), 400

    cafe_all = db.select(Cafe)
    result = db.session.execute(cafe_all.where(Cafe.location == query_location))
    all_cafes = result.scalars().all()

    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():

    # Convert common truthy/falsey strings from Postman
    def to_bool(value: str) -> bool:
        return str(value).strip().lower() in {"true", "1", "yes", "y", "on"}

    # Define the two main actors of the function
    form_input = request.form
    new_cafe = Cafe()
    # Build the model dynamically from incoming form fields
    # NOTE: each 'column' is the SQLAlchemy metadata, not the row value
    for column in new_cafe.__table__.columns: # type: ignore[reportAttributeAccessIssue]

        # Let id, as the primary key, being set by SQLAlchemy
        if column.name == "id":
            continue

        # Use the column name to retrive the related form input value
        raw_value = form_input.get(column.name)

        # If field is missing entirely
        if raw_value is None:
            # Check if the column can be nullable
            if not column.nullable:
                return jsonify({"Bad request": f"Missing required field '{column.name}'"}), 400

            # Optional field here, leave it none or default
            continue

        # Convert booleans from strings
        if isinstance(column.type, Boolean):
            value = to_bool(raw_value)
        else:
            value = raw_value

        # Dynamically set the attribute on the SQLAlchemy model
        setattr(new_cafe, column.name, value)

    db.session.add(new_cafe)
    db.session.commit()

    # new_cafe = Cafe(
    #     name=request.form.get("name"), # type: ignore[reportCallIssue]
    #     map_url=request.form.get("map_url"), # type: ignore[reportCallIssue]
    #     img_url=request.form.get("img_url"), # type: ignore[reportCallIssue]
    #     location=request.form.get("location"), # type: ignore[reportCallIssue]
    #     seats=request.form.get("seats"), # type: ignore[reportCallIssue]
    #     has_toilet=bool(request.form.get("has_toilet")), # type: ignore[reportCallIssue]
    #     has_wifi=bool(request.form.get("has_wifi")), # type: ignore[reportCallIssue]
    #     has_sockets=bool(request.form.get("has_sockets")), # type: ignore[reportCallIssue]
    #     can_take_calls=bool(request.form.get("can_take_calls")), # type: ignore[reportCallIssue]
    #     coffee_price=request.form.get("coffee_price"), # type: ignore[reportCallIssue]
    # )
    # db.session.add(new_cafe)
    # db.session.commit()

    return jsonify(response={"success":"Successfully added the new cafe"})


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
