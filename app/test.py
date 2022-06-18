from queries import Customer, Employee, Estate, Contract

################## CLASS BASE ##################

# CUSTOMER
# custom = Customer()


# res = custom.search("00444444")
# print(res)

# create
# custom.create("reza", "rezaii", '00444444', '+9891244444', email="reza@mail.com", address="tehran, pasdaran")

# search
# res = custom.search("rez")
# print(res)

# delete
# custom.delete(4)

####################################

# EMPLOYEE
# emp = Employee()

# create
# emp.create('reza', '007', 'reza')

# search
# res = emp.search("ali")
# print(res)

# delete
# emp.delete(id=3)

####################################

# ESTATE
# est = Estate()
# customer = Customer()

# create
# owners = customer.search('amir')
# print(owners)
# est.create(postal_code='12321', owner=owners)

# search
# res = est.search("12321")
# print(res[0].owner[0].first_name)

# delete
# est.delete(id=2)

####################################

# CONTRACT
# contract = Contract()
# estate = Estate()
# customer = Customer()
# employee = Employee()

# create
# estate1 = estate.search(postal_code='12345')[0]
# buyer = customer.search('amir')
# seller = customer.search('ali')
# employee1 = employee.search('hamid')[0]
# contract.create(estate=estate1, buyer=buyer, seller=seller, employee=employee1, contract_type="buy/sell")

# search
# res = contract.search(id=2)
# print(res)

# delete
# contract.delete(id=2)


################## CLASS BASE WITH STATIC METHODS ##################

# CUSTOMER


# create
# Customer.create("shokoh", "hamidi", '13213312', '+98938432422', email="divesepidpydarband@mail.com", address="ghazvin, pasdaran")

# search
# res = Customer.search("rez")
# print(res)

# delete
# Customer.delete(4)

# get by id
# res = Customer.get_by_id("1")
# print(res)
####################################

# EMPLOYEE

# create
# Employee.create(username='baran1200', password='12212', first_name='baran', last_name="habibi")

# search
# res = Employee.search("ali")
# print(res)

# delete
# Employee.delete(id=3)

####################################

# ESTATE

# create
# owners = Customer.search('shokoh')
# print(owners)
# Estate.create(postal_code='4234234', owner=owners)

# search
# res = Estate.search("12321")
# print(res[0].owner[0].first_name)

# delete
# Estate.delete(id=2)


# owner = Customer.get_by_id(2)
# est = Estate.get_by_id(1)
# print(est.owner.append(owner))
# Estate.add_owner(1, 2)

####################################

# CONTRACT

# create
estate1 = Estate.get_by_id(1)
buyer = Customer.get_by_id(3)
seller = Customer.get_by_id(1)
employee1 = Employee.get_by_id(1)
Contract.create(estate=estate1, buyer=[buyer], seller=[seller], employee=employee1, contract_type="buy/sell")

# search
# res = Contract.search(id=2)
# print(res)

# delete
# Contract.delete(id=2)
