from model.models import Products

class ProductsDAOORM:
    def __init__(self, session):
        self.session = session

    def retornaIDPeloProductName(self, productName):
        result = self.session.query(Products.productid)\
            .filter(Products.productname.like(productName))\
            .scalar()
        return result
