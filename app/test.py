from queries import Customer, Employee, Estate, Contract


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
