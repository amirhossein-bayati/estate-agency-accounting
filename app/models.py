from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

import os
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("host")
username = os.getenv("host_username")
password = os.getenv("host_password")
db_name = os.getenv("db_name")

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(username, password, host, db_name)
# conn = "sqlite:///db.sqlite"

# conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(username, password, host, db_name)
# conn = f'mssql+pymssql://@DESKTOP-K105VCB\\amirhossein:estate_agency:?charset=utf8'

# DB_HOST = "localhost"
# DB_PASSWORD = ""
# DB_USER = "estate_agency"

# conn = f'mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}?charset=utf8'
# conn = f"mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/?charset=utf8"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db, compare_type=True)
db.init_app(app)


estate_owners = db.Table('estate_owner',
	db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True),
	db.Column('estate_id', db.Integer, db.ForeignKey('estate.id'), primary_key=True),
)

customer_contract_buy = db.Table('customer_contract_buy',
	db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True),
	db.Column('contract_id', db.Integer, db.ForeignKey('contract.id'), primary_key=True),
)

customer_contract_sell = db.Table('customer_contract_sell',
	db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True),
	db.Column('contract_id', db.Integer, db.ForeignKey('contract.id'), primary_key=True),
)


class Employee(db.Model):
	def __repr__(self):
		return f'<Employee {self.username}>'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(50), unique=True, nullable=False)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	identity_card = db.Column(db.String(12), unique=True)
	mobile = db.Column(db.String(13), unique=True)
	email = db.Column(db.String(120), unique=True)
	position = db.Column(db.String(20))
	salary = db.Column(db.Float)
	total_sales = db.Column(db.Integer, default=0)




class Customer(db.Model):
	def __repr__(self):
		return f'<Customer {self.first_name} {self.last_name}>'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	identity_card = db.Column(db.String(12), unique=True)
	mobile = db.Column(db.String(13), unique=True)
	email = db.Column(db.String(120), unique=True)
	address = db.Column(db.String(250))




class Estate(db.Model):
	def __repr__(self):
		return f'Estate {self.postal_code}'

	id = db.Column(db.Integer, primary_key=True)
	postal_code = db.Column(db.String(20), unique=True)
	owner = db.relationship('Customer', secondary=estate_owners, backref=db.backref('estates', lazy='subquery'))
	address = db.Column(db.String(250))
	estate_type = db.Column(db.String(50))
	floor_space = db.Column(db.Float)
	number_of_bedrooms = db.Column(db.Integer)
	number_of_bathrooms = db.Column(db.Integer)
	number_of_parking = db.Column(db.Integer)
	floor = db.Column(db.Integer)
	number_of_floors = db.Column(db.Integer)
	number_of_unit_per_floor = db.Column(db.Integer)
	elevator = db.Column(db.Boolean)
	made_year = db.Column(db.Integer)
	description = db.Column(db.Text)





class Contract(db.Model):
	def __repr__(self):
		return f'<Contract {self.id}>'

	id = db.Column(db.Integer, primary_key=True)
	estate_id = db.Column(db.Integer, db.ForeignKey("estate.id"), nullable=True)
	estate = db.relationship('Estate', backref="contracts")

	agent_id = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable=True)
	employee = db.relationship('Employee', backref='contracts')

	buyer = db.relationship('Customer', secondary=customer_contract_buy, backref='buy_contract')
	seller = db.relationship('Customer', secondary=customer_contract_sell, backref='sell_contract')

	contract_type = db.Column(db.String(30))

	payment_amount = db.Column(db.Float)
	profit = db.Column(db.Float)
	date_signed = db.Column(db.DateTime, default=datetime.utcnow())
	description = db.Column(db.Text(500))





