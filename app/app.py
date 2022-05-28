from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format('root', '', 'localhost', 'estate_agency')
# conn = 'sqlite:///test.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn

db = SQLAlchemy(app)

class Employee(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	identity_card = db.Column(db.String(12))
	mobile = db.Column(db.String(12))
	phone_number = db.Column(db.String(12))
	email = db.Column(db.String(120))
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	fathers_name = db.Column(db.String(50))
	address = db.Column(db.String(250))
	salary = db.column(db.Float)
	total_sales = db.Column(db.Integer, default=0)
	position = db.Column(db.String(20))

estate_owners = db.Table('EstateOwner',
	db.column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True),
	db.column('estate_id', db.Integer, db.ForeignKey('estate.id'), primary_key=True),
)

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	identity_card = db.Column(db.String(12))
	mobile = db.Column(db.String(12))
	phone_number = db.Column(db.String(12))
	email = db.Column(db.String(120))
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	fathers_name = db.Column(db.String(50))
	address = db.Column(db.String(250))
	estates = db.relationship('Estate', secondary=estate_owners, backref=db.backref('customer', lazy='subquery'))


class Estate(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	postal_code = db.Column(db.String(20))
	estate_type = db.Column(db.String(50))
	floor_space = db.Column(db.Float)
	number_of_balconies = db.Column(db.Integer, default=0)
	number_of_bedrooms = db.Column(db.Integer, default=0)
	number_of_bathrooms = db.column(db.Integer, default=0)
	number_of_parking = db.Column(db.Integer, default=0)
	floor = db.column(db.Integer, nullable=False)
	number_of_floors = db.Column(db.Integer)
	number_of_unit_per_floor = db.Column(db.Integer)
	elevator = db.Column(db.Boolean)
	made_year = db.Column(db.DateTime, default=datetime.utcnow())
	# address = db.column(db.Text(500))
	description = db.Column(db.Text)
	

@app.route('/')
def index():
	return "Hello, World"



if __name__ == '__main__':
	app.run(debug=True)