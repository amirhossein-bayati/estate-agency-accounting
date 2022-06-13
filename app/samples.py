import models
from models import app, db

# Make Customer Instance
customer1 = models.Customer(
    first_name="Amirhossein",
    last_name="bayati",
    identity_card='0311111111',
    mobile='+989121111111',
    email='amir@mail.com',
    address="krj"
)
customer2 = models.Customer(
    first_name="Mohammad",
    last_name="Norozi",
    identity_card='002222222',
    mobile='+989192222222',
    email='mohammad@mail.com',
    address="tehran"
)

db.session.add(customer1)
db.session.add(customer2)
db.session.commit()

# Make Employee Instance
employee1 = models.Employee(
    username="hamid021",
    password="hamid123",
    first_name="hamid",
    last_name="hamidi",
    identity_card="2121212121",
    mobile="099999999",
    email='hamid@mail.com',
    salary=6000000,
    total_sales=0,
    position="leader"
)
db.session.add(employee1)
db.session.commit()

# Make Estate Instance
estate1 = models.Estate(
    owner=[customer1, customer2],
    postal_code='12345',
    estate_type='apartment',
    address="tehran, niavaran",
    floor_space=110,
    number_of_bedrooms=2,
    number_of_bathrooms=1,
    number_of_parking=1,
    floor=2,
    number_of_floors=3,
    number_of_unit_per_floor=2,
    elevator=False,
    made_year=2000,
    description="with road view"
)

db.session.add(estate1)
db.session.commit()

# Make Contract Instance
contract1 = models.Contract(
    estate=estate1,
    employee=employee1,
    buyer=[customer1],
    seller=[customer2],
    contract_type="rent",
    payment_amount=10000000,
    profit=2000000,
)
db.session.add(contract1)
db.session.commit()
