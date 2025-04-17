from model.models import Orders, OrderDetails, Customers, Employees, Products
from sqlalchemy.orm import Session

class OrdersDAOORM:
    def __init__(self, session: Session):
        self.session = session
        
    def retornaNovoIDInsercao(self):
        max_id = self.session.query(Orders.orderid).order_by(Orders.orderid.desc()).first()
        return (max_id[0] + 1) if max_id and max_id[0] else 1


    def inserePedidoComDetalhes(self, order_id, customer_id, employee_id, order_date, details):
        novoPedido = Orders(
            orderid=order_id,
            customerid=customer_id,
            employeeid=employee_id,
            orderdate=order_date
        )

        for detalhe in details:
            novoDetalhe = OrderDetails(
                orderid=order_id,
                productid=detalhe["product_id"],
                quantity=detalhe["quantity"],
                unitprice=detalhe["unit_price"]
            )
            novoPedido.order_details.append(novoDetalhe)

        self.session.add(novoPedido)
        return 

    def retornaRelatorioPedido(self, orderID):
        resultados = self.session.query(
            Orders.orderid,
            Orders.orderdate,
            Customers.companyname,
            (Employees.firstname + ' ' + Employees.lastname).label('vendedor'),
            Products.productname,
            OrderDetails.quantity,
            OrderDetails.unitprice
        ).join(Employees, Orders.employeeid == Employees.employeeid) \
         .join(Customers, Orders.customerid == Customers.customerid) \
         .join(OrderDetails, Orders.orderid == OrderDetails.orderid) \
         .join(Products, OrderDetails.productid == Products.productid) \
         .filter(Orders.orderid == orderID) \
         .order_by(Orders.orderid.desc()) \
         .all()

        return resultados
