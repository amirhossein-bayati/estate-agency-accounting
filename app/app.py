from flask import Flask
from flask_sqlalchemy import SQLAlchemy

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format('root', '', 'localhost', 'estate_agency')
# conn = 'sqlite:///test.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conn

db = SQLAlchemy(app)

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

@app.route('/')
def index():
	return "Hello, World"



if __name__ == '__main__':
	app.run(debug=True)