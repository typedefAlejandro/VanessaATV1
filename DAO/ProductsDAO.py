
class ProductsDAO():
    def __init__(self):
        pass
        
    def retornaIDPeloProductName(self, cursor, productName):
        query = f"""SELECT productid 
                FROM northwind.products
                WHERE productname LIKE '{productName}'"""
        cursor.execute(query)
        return cursor.fetchone()[0]
    