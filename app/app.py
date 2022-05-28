from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format('root', '', 'localhost', 'estate_agency')
# conn = 'sqlite:///test.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn

db = SQLAlchemy(app)


estate_owners = db.Table('EstateOwner',
	db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
	db.Column('estate_id', db.Integer, db.ForeignKey('estate.id')),
)

customer_contract = db.Table('contractAgent',
	db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
	db.Column('contract_id', db.Integer, db.ForeignKey('contract.id')),
)


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
	salary = db.Column(db.Float)
	total_sales = db.Column(db.Integer, default=0)
	position = db.Column(db.String(20))
	# contracts = db.relationship('Contract', secondary=contract_agent, backref=db.backref('employee', lazy='subquery'))
	contracts = db.relationship('Contract', backref='employee', cascade="all, delete")


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
	contracts = db.relationship('Contract', secondary=customer_contract, backref=db.backref('customer', lazy='subquery'))

class Estate(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	postal_code = db.Column(db.String(20))
	estate_type = db.Column(db.String(50))
	floor_space = db.Column(db.Float)
	number_of_balconies = db.Column(db.Integer, default=0)
	number_of_bedrooms = db.Column(db.Integer, default=0)
	number_of_bathrooms = db.Column(db.Integer, default=0)
	number_of_parking = db.Column(db.Integer, default=0)
	floor = db.Column(db.Integer, nullable=False)
	number_of_floors = db.Column(db.Integer)
	number_of_unit_per_floor = db.Column(db.Integer)
	elevator = db.Column(db.Boolean)
	made_year = db.Column(db.DateTime, default=datetime.utcnow())
	address = db.Column(db.Text(500))
	description = db.Column(db.Text)

	# contracts = db.relationship('Contract', backref="estates", cascade="all, delete")


class Contract(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	estate_id = db.Column(db.Integer, db.ForeignKey("estate.id"), nullable=True)
	estate = db.relationship('Contract', backref="contracts", cascade="all, delete")

	agent_id = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable=True)
	buyer = db.relationship('Customer', secondary=customer_contract, backref='contract')
	seller = db.relationship('Customer', secondary=customer_contract, backref='contract')
	contract_type = db.Column(db.String(30))
	payment_amount = db.Column(db.Float)
	profit = db.Column(db.Float)
	date_signed = db.Column(db.DateTime, default=datetime.utcnow())
	description = db.Column(db.Text(500))



@app.route('/new-customer')
def index():
	customer1 = Customer(
		identity_card='1111111',
		mobile='+9891211111',
		phone_number='026322222',
		email='mail@mail.com',
		first_name='amir'
	)
	db.session.add(customer1)
	db.session.commit()



if __name__ == '__main__':
	app.run(debug=True)