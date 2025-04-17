
class OrdersDAO():
    def __init__(self):
        pass
        
    def retornaNovoIDInsercao(self, cursor):
        query = """SELECT MAX(orderid) + 1 FROM northwind.orders"""
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] if result else None
    
    def inserePedido(self, cursor, orderid, customerid, employeeid, orderdate):
        query = f"""INSERT INTO northwind.orders 
                    (orderid, customerid, employeeid, orderdate)
                    VALUES ({orderid}, '{customerid}', {employeeid}, '{orderdate}')"""
        cursor.execute(query)
        return
    
    def retornaRelatorioPedido(self, cursor, orderID):
        query = f"""SELECT o.orderid, o.orderdate, c.companyname, concat(e.firstname, ' ', e.lastname), p.productname, d.quantity, d.unitprice
                    FROM northwind.orders o
                    JOIN northwind.employees e
                        ON e.employeeid = o.employeeid
                    JOIN northwind.customers c
                        ON o.customerid = c.customerid
                    JOIN northwind.order_details d
                        ON d.orderid = o.orderid
                    JOIN northwind.products p 
                        ON p.productid = d.productid
                    WHERE o.orderid = '{orderID}'
                    ORDER BY o.orderid DESC"""
        cursor.execute(query)
        return cursor.fetchall()
