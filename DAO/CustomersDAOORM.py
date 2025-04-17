from model.models import Customers

class CustomersDAOORM:
    def __init__(self, session):
        self.session = session

    def retornaIDPeloCompanyName(self, companyName):
        result = self.session.query(Customers.customerid)\
            .filter(Customers.companyname.like(companyName))\
            .scalar()
        return result
