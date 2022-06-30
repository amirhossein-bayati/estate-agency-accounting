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
    first_name="shaghayegh",
    last_name="naghizadeh",
    identity_card='002222222',
    mobile='+989192222222',
    email='shaghayegh@mail.com',
    address="tehran"
)

customer3 = models.Customer(
    first_name="ali",
    last_name="alavi",
    identity_card='003333333',
    mobile='+989193333333',
    email='ali@mail.com',
    address="shiraz"
)

customer4 = models.Customer(
    first_name="parham",
    last_name="parhami",
    identity_card='004444444',
    mobile='+989124444444',
    email='parham@mail.com',
    address="ghazvin"
)

customer5 = models.Customer(
    first_name="mahsa",
    last_name="parsa",
    identity_card='00555555',
    mobile='+9891255555',
    email='mahsa@mail.com',
    address="tehran"
)
db.session.add(customer1)
db.session.add(customer2)
db.session.add(customer3)
db.session.add(customer4)
db.session.add(customer5)

db.session.commit()

# Make Employee Instance
employee1 = models.Employee(
    username="hamid",
    password="hamid123",
    first_name="hamid",
    last_name="hamidi",
    identity_card="1111111",
    mobile="0991211111",
    email='hamid@mail.com',
    salary=6000000,
    total_sales=0,
    position="leader"
)
employee2 = models.Employee(
    username="ali",
    password="ali123",
    first_name="ali",
    last_name="zamani",
    identity_card="2222222",
    mobile="0991222222",
    email='ali@mail.com',
    salary=3000000,
    total_sales=0,
    position="simple"
)
employee3 = models.Employee(
    username="ahmad",
    password="ahmad123",
    first_name="ahmad",
    last_name="akbari",
    identity_card="3333333",
    mobile="0991233333",
    email='ahmad@mail.com',
    salary=10000000,
    total_sales=0,
    position="manager"
)
db.session.add(employee1)
db.session.add(employee2)
db.session.add(employee3)

db.session.commit()


# Make Estate Instance
estate1 = models.Estate(
    owner=[customer1, customer5],
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
    made_year=2020,
    description="with road view"
)

estate2 = models.Estate(
    owner=[customer5],
    postal_code='11111',
    estate_type='apartment',
    address="tehran, pasdaran",
    floor_space=90,
    number_of_bedrooms=2,
    number_of_bathrooms=1,
    number_of_parking=2,
    floor=3,
    number_of_floors=4,
    number_of_unit_per_floor=1,
    elevator=True,
    made_year=2010,
    description="with MDF cabinets"
)

estate3 = models.Estate(
    owner=[customer2, customer3],
    postal_code='2222',
    estate_type='villa',
    address="tehran, shemron",
    floor_space=550,
    number_of_bedrooms=5,
    number_of_bathrooms=3,
    number_of_parking=5,
    floor=1,
    number_of_floors=1,
    number_of_unit_per_floor=1,
    elevator=False,
    made_year=2010,
    description="with pool and green Field"
)

db.session.add(estate1)
db.session.add(estate2)
db.session.add(estate3)

db.session.commit()

# Make Contract Instance
contract1 = models.Contract(
    estate=estate1,
    employee=employee1,
    buyer=[customer1],
    seller=[customer4],
    contract_type="buy/sell",
    payment_amount=10000000,
    profit=2000000,
)

contract2 = models.Contract(
    estate=estate2,
    employee=employee1,
    buyer=[customer2],
    seller=[customer5],
    contract_type="rent",
    payment_amount=500000,
    profit=1000,
)

db.session.add(contract1)
db.session.add(contract2)

db.session.commit()
