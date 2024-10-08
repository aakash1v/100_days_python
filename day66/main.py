from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
from werkzeug.exceptions import NotFound



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
        # Method 1
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    # })

    return jsonify(cafe=random_cafe.to_dict())

    
        
@app.route("/all")
def all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify( cafes=[cafe.to_dict() for cafe in all_cafes ])

@app.route('/search') 
def get_cafe():
    loc = request.args['loc']
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc.capitalize() )).scalars().all()
    if cafes:
        return jsonify(cafe = [cafe.to_dict() for cafe in cafes ]), 200
    else:
        return jsonify(error={'Not Found': "There is no cafe in this location"}), 404
    

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=int(request.form.get("sockets")),
        has_wifi=int(request.form.get("wifi")),
        has_toilet=int(request.form.get("toilet")),
        can_take_calls=int(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response= {"success":"Successfully added new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    print(cafe,0)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response= {'success': 'Price is Successfully updated..'}),200
    else:
        return jsonify(error={"Not Found": "Sorry a Cafe with this id doesn't exist in our database."}), 404

# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['Delete'])
def delete_cafe(cafe_id):
    apikey= request.args.get('api-key')
    if apikey == 'TopSecretApiKey':
        try:
            cafe = db.get_or_404(Cafe, cafe_id)
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f" Cafe with cafe_id {cafe_id} is successfully deleted."})
        except NotFound:
            return jsonify(error={'Not Found': "Cafe with this cafe id doesn't exist.."})
        except Exception as e:
            return jsonify(error=f'{e}')
    else:
        return jsonify(error={'Forbidden': "Sorry, this is not allowed. Make sure u have the correct apikey."}), 403


if __name__ == '__main__':
    app.run(debug=True)
