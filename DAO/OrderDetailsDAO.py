
class OrderDetailsDAO():
    def __init__(self):
        pass
        
    def insereDetalhesPedido(self, cursor, orderID, productID, unitPrice, quantity):
        query = f""" INSERT INTO northwind.order_details
                    (orderid, productid, unitprice, quantity)
                    VALUES ({orderID}, '{productID}',
                            {unitPrice}, '{quantity}')"""
        cursor.execute(query)
        return