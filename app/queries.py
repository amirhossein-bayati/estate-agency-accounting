import models
from models import app, db
from sqlalchemy import or_


class Customer:

    @staticmethod
    def create(first_name=None, last_name=None, identity_card=None, mobile=None, email=None, address=None):

        existing = Customer.check_identity_number(identity_card)
        assert not existing, "identity card exists"

        customer = models.Customer(
            first_name=first_name,
            last_name=last_name,
            identity_card=identity_card,
            mobile=mobile,
            email=email,
            address=address
        )

        db.session.add(customer)
        db.session.commit()

    @staticmethod
    def search(keyword) -> list:
        result = models.Customer.query.filter(or_(
            models.Customer.first_name.like(f'%{keyword}%'),
            models.Customer.last_name.like(f'%{keyword}%'),
            models.Customer.identity_card == keyword,
        )).all()
        return result

    @staticmethod
    def check_identity_number(ic) -> bool:
        result = models.Customer.query.filter_by(identity_card=ic).all()
        if result:
            return True
        else:
            return False

    @staticmethod
    def delete(id):
        try:
            cutomer = models.Customer.query.filter_by(id=id).first()
            db.session.delete(cutomer)
            db.session.commit()
        except Exception as err:
            print(err)

    @staticmethod
    def get_by_id(id) -> object:
        res = models.Customer.query.filter_by(id=id).first()
        return res


    @staticmethod
    def get_by_identity_card(id) -> object:
        res = models.Customer.query.filter_by(identity_card=id).first()
        return res


class Employee:

    @staticmethod
    def create(username, password, first_name=None, last_name=None, identity_card=None, mobile=None, email=None,
               position=None, salary=None, total_sales=0):
        existing = Employee.check_identity_number(identity_card)
        assert not existing, "identity card exists"

        employee = models.Employee(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            identity_card=identity_card,
            mobile=mobile,
            email=email,
            position=position,
            salary=salary,
            total_sales=total_sales,
        )

        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def search(keyword) -> list:
        result = models.Employee.query.filter(or_(
            models.Employee.first_name.like(f'%{keyword}%'),
            models.Employee.last_name.like(f'%{keyword}%'),
            models.Employee.identity_card == keyword,
        )).all()
        return result

    @staticmethod
    def delete(id):
        try:
            employee = models.Employee.query.filter_by(id=id).first()
            db.session.delete(employee)
            db.session.commit()
        except Exception as err:
            print(err)

    @staticmethod
    def check_identity_number(ic) -> bool:
        result = models.Employee.query.filter_by(identity_card=ic).all()
        if result:
            return True
        else:
            return False

    @staticmethod
    def get_by_id(id) -> object:
        res = models.Employee.query.filter_by(id=id).first()
        return res

    @staticmethod
    def get_by_identity_card(id) -> object:
        res = models.Employee.query.filter_by(identity_card=id).first()
        return res

class Estate:

    @staticmethod
    def create(postal_code: str = None, owner: list = None, address=None, estate_type=None, floor_space=None,
               number_of_bedrooms=0,
               number_of_bathrooms=0, number_of_parking=0, floor=0, number_of_floors=None,
               number_of_unit_per_floor=None, elevator=None,
               made_year=None, description=None):

        owners = []
        existing = Estate.check_postal_number(postal_code)
        assert not existing, "postal code exists"

        for i in owner:
            customer = Customer.get_by_identity_card(i)
            print(customer)
            # check if customer exists
            existing = Customer.check_identity_number(i)
            print(existing)
            assert existing, "customer does not exist"

            owners.append(customer)
        
        estate = models.Estate(
            owner=owners,
            postal_code=postal_code,
            estate_type=estate_type,
            address=address,
            floor_space=floor_space,
            number_of_bedrooms=number_of_bedrooms,
            number_of_bathrooms=number_of_bathrooms,
            number_of_parking=number_of_parking,
            floor=floor,
            number_of_floors=number_of_floors,
            number_of_unit_per_floor=number_of_unit_per_floor,
            elevator=elevator,
            made_year=made_year,
            description=description
        )

        db.session.add(estate)
        db.session.commit()

    @staticmethod
    def search(postal_code) -> list:
        result = models.Estate.query.filter_by(postal_code=postal_code).all()
        if result:
            return result
        else:
            return result

    @staticmethod
    def delete(id):
        try:
            estate = models.Estate.query.filter_by(id=id).first()
            db.session.delete(estate)
            db.session.commit()
        except Exception as err:
            print(err)

    @staticmethod
    def check_postal_number(code) -> bool:
        result = models.Estate.query.filter_by(postal_code=code).all()
        if result:
            return True
        else:
            return False

    @staticmethod
    def get_by_id(id) -> object:
        res = models.Estate.query.filter_by(id=id).first()
        return res

    @staticmethod
    def add_owner(estate_id, customer_id):
        customer = Customer.get_by_id(customer_id)
        est = Estate.get_by_id(estate_id)
        est.owner.append(customer)
        db.session.commit()

    @staticmethod
    def remove_owner(estate_id, customer_id) -> bool:
        customer = Customer.get_by_id(customer_id)
        est = Estate.get_by_id(estate_id)
        owners = est.owner
        assert customer in owners, f"Customer with \"{customer_id}\" id didnt owned this estate"
        if customer in owners:
            owners.remove(customer)
            est.owner = owners
            db.session.commit()
            return True
        else:
            return False


    @staticmethod
    def get_by_postal_number(code):
        result = models.Estate.query.filter_by(postal_code=code).first()
        return result

class Contract:

    @staticmethod
    def create(estate_postal_code: str, employee_identity_card: str, buyer: list, seller: list, contract_type: str = None,
               payment_amount: float = None, profit: float = None):
        
        # print(buyer)
        # print(seller)
        
        buyers=[]
        sellers=[]

        # check if estate exists
        existing = Estate.check_postal_number(estate_postal_code)
        assert existing, "estate does not exist"
        estate = Estate.get_by_postal_number(estate_postal_code)

        # print("==========================")
               

        # check if employee exists
        existing = Employee.check_identity_number(employee_identity_card)
        assert existing, "employee does not exist"
        employee = Employee.get_by_identity_card(employee_identity_card)

        # check if buyer exists
        for i in buyer:
            existing = Customer.check_identity_number(i)
            assert existing, "buyer does not exist"
            buyers.append(Customer.get_by_identity_card(i))


        # check if seller exists
        for i in seller:
            existing = Customer.check_identity_number(i)
            assert existing, "seller does not exist"
            sellers.append(Customer.get_by_identity_card(i))



        # print(buyers)
        # print(sellers)

        contract = models.Contract(
            estate=estate,
            employee=employee,
            buyer=buyers,
            seller=sellers,
            contract_type=contract_type,
            payment_amount=payment_amount,
            profit=profit,
        )
        db.session.add(contract)
        db.session.commit()


        if contract_type=='buy/sell':
            for i in buyers:
                Estate.add_owner(estate.id, i.id)
            for i in sellers:
                Estate.remove_owner(estate.id, i.id)

    @staticmethod
    def search(id) -> list:
        result = models.Contract.query.filter_by(id=id).all()
        if result:
            return result
        else:
            return result

    @staticmethod
    def delete(id):
        try:
            contract = models.Contract.query.filter_by(id=id).first()
            db.session.delete(contract)
            db.session.commit()
        except Exception as err:
            print(err)

    @staticmethod
    def get_by_id(id) -> object:
        res = models.Contract.query.filter_by(id=id).first()
        return res
