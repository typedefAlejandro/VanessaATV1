
class CustomersDAO():
    def __init__(self):
        pass
        
    def retornaIDPeloCompanyName(self, cursor, companyName):
        query = f"""SELECT customerid
                FROM northwind.customers
                WHERE companyname LIKE '{companyName}'"""
        cursor.execute(query)
        return cursor.fetchone()[0]