
class ProductsDAO():
    def __init__(self):
        pass
        
    def retornaIDPeloProductName(self, cursor, productName):
        query = f"""SELECT productid 
                FROM northwind.products
                WHERE productname LIKE '{productName}'"""
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] if result else None
    