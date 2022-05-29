from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format('root', '', 'localhost', 'estate_agency')
# conn = 'sqlite:///test.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn

db = SQLAlchemy(app)


estate_owners = db.Table('estate_owner',
	db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
	db.Column('estate_id', db.Integer, db.ForeignKey('estate.id')),
)

customer_contract_buy = db.Table('customer_contract_buy',
	db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
	db.Column('contract_id', db.Integer, db.ForeignKey('contract.id')),
)

customer_contract_sell = db.Table('customer_contract_sell',
	db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
	db.Column('contract_id', db.Integer, db.ForeignKey('contract.id')),
)

class Employee(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	fathers_name = db.Column(db.String(50))
	identity_card = db.Column(db.String(12), unique=True)
	mobile = db.Column(db.String(12), unique=True)
	phone_number = db.Column(db.String(12), unique=True)
	email = db.Column(db.String(120), unique=True)
	address = db.Column(db.String(250))
	position = db.Column(db.String(20))
	salary = db.Column(db.Float)
	total_sales = db.Column(db.Integer, default=0)
	# contracts = db.relationship('Contract', secondary=contract_agent, backref=db.backref('employee', lazy='subquery'))
	# contracts = db.relationship('Contract', backref='employee', cascade="all, delete")


class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	fathers_name = db.Column(db.String(50))
	identity_card = db.Column(db.String(12), unique=True)
	mobile = db.Column(db.String(12), unique=True)
	phone_number = db.Column(db.String(12), unique=True)
	email = db.Column(db.String(120), unique=True)
	address = db.Column(db.String(250))


	# estates = db.relationship('Estate', secondary=estate_owners, backref=db.backref('customer', lazy='subquery'))
	# contracts = db.relationship('Contract', secondary=customer_contract, backref=db.backref('customer', lazy='subquery'))

class Estate(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	postal_code = db.Column(db.String(20), unique=True)
	owner = db.relationship('Customer', secondary=estate_owners, backref=db.backref('estates', lazy='subquery'))
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
	made_year = db.Column(db.Integer)
	address = db.Column(db.Text(500))
	description = db.Column(db.Text)


# contracts = db.relationship('Contract', backref="estates", cascade="all, delete")


class Contract(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	estate_id = db.Column(db.Integer, db.ForeignKey("estate.id"), nullable=True)
	estate = db.relationship('Estate', backref="contracts", cascade="all, delete")

	agent_id = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable=True)
	employee = db.relationship('Employee', backref='contracts', cascade="all, delete")

	# buyer_id = db.Column(db.Integer, db.ForeignKey("buyer.id"), nullable=True)
	# seller_id = db.Column(db.Integer, db.ForeignKey("seller.id"), nullable=True)
	buyer = db.relationship('Customer', secondary=customer_contract_buy, backref='buy_contract')
	seller = db.relationship('Customer', secondary=customer_contract_sell, backref='sell_contract')

	# contracts = db.relationship('Contract', secondary=customer_contract, backref=db.backref('customer', lazy='subquery'))
	contract_type = db.Column(db.String(30))
	payment_amount = db.Column(db.Float)
	profit = db.Column(db.Float)
	date_signed = db.Column(db.DateTime, default=datetime.utcnow())
	description = db.Column(db.Text(500))



@app.route('/new-customer')
def create_customer():
	arr = ['amir', 'ali', 'mammad', 'mahsa', 'zahra']
	for i, name in enumerate(arr):
		customer1 = Customer(
			identity_card=f'{i}{i}{i}{i}{i}',
			mobile=f'+98{i}{i}{i}{i}',
			phone_number=f'026{i}{i}{i}{i}{i}',
			email=f'{i}{i}{i}{i}{i}@mail.com',
			first_name=name
		)
		db.session.add(customer1)
		db.session.commit()
	return "DONE"


@app.route('/new-employee')
def create_employee():
	arr = ['david', 'jafar', 'kazem', 'akbar']
	for i, name in enumerate(arr):
		employee1 = Employee(
			identity_card=f'{i}{i}{i}{i}{i}',
			mobile=f'+98{i}{i}{i}{i}{i}{i}',
			phone_number=f'026{i}{i}{i}{i}{i}',
			email=f'{i}{i}{i}{i}{i}@mail.com',
			first_name=name,
			salary=int(f"{i}{i}{i}{i}{i}")
		)

		db.session.add(employee1)
		db.session.commit()
	return "DONE"


@app.route('/new-estate')
def create_estate():
	owner1 = Customer.query.filter_by(id=2).first()
	owner2 = Customer.query.filter_by(id=3).first()

	# print("========================")
	# print(owner)
	# print(type(owner))
	# print("========================")
	estate1 = Estate(
		postal_code=222222,
		floor_space=222222,
		floor=22,
		number_of_floors=2,
		made_year=2222,
		owner=[owner1, owner2]
	)

	db.session.add(estate1)
	db.session.commit()
	return "DONE"


@app.route('/show-estate-owner')
def show_estate_owner():
	# estate = Estate.query.filter_by(postal_code=42).first()
	# owner = estate.owner
	# print("\n\n\n++++++++++++++++++")
	# print(owner)
	# print("++++++++++++++++++\n\n\n")
	# return owner[0].first_name
	contract = Contract.query.filter_by(id=1).first()
	seller = contract.seller
	seller = seller[0].first_name
	buyer = contract.buyer
	buyer = buyer[0].first_name
	agent = contract.employee.first_name


	print("\n\n\n\n\n", contract.buyer, contract.seller, "\n\n\n\n\n\n")
	tmp = seller + " -> " + buyer + " -> " + agent

	return tmp


@app.route('/create-contract')
def create_contract():
	estate = Estate.query.filter_by(id=1).first()
	agent = Employee.query.filter_by(id=1).first()
	buyer = Customer.query.filter_by(id=1).first()
	seller = Customer.query.filter_by(id=2).first()
	contract1 = Contract(
		estate=estate,
		employee=agent,
		buyer=[buyer],
		seller=[seller],
		contract_type="rent",
		payment_amount=10000000
	)
	db.session.add(contract1)
	db.session.commit()
	return "done contract"

if __name__ == '__main__':
	app.run(debug=True)