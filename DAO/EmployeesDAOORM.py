from model.models import Employees, Orders, OrderDetails
from sqlalchemy import func

class EmployeesDAOORM:
    def __init__(self, session):
        self.session = session

    def retornaIDpeloEmployeeName(self, employeeName):
        return self.session.query(Employees.employeeid)\
            .filter((Employees.firstname + ' ' + Employees.lastname).like(employeeName))\
            .scalar()

    def retornaSomaVendasFuncionarioPorIntervalo(self, inicio, fim):
        nome = func.concat(Employees.firstname, ' ', Employees.lastname).label("name")

        result = self.session.query(
            nome,
            func.count(func.distinct(Orders.orderid)).label("quantidade_pedidos"),
            func.sum(OrderDetails.unitprice * OrderDetails.quantity).label("valor_vendas")
        ).join(Orders, Employees.employeeid == Orders.employeeid) \
         .join(OrderDetails, Orders.orderid == OrderDetails.orderid) \
         .filter(Orders.orderdate.between(inicio, fim)) \
         .group_by(nome) \
         .order_by(func.sum(OrderDetails.unitprice * OrderDetails.quantity).desc()) \
         .all()

        return result

    def retornaSomaPedidosFuncionarioPorIntervalo(self, inicio, fim):
        nome = func.concat(Employees.firstname, ' ', Employees.lastname).label("name")

        result = self.session.query(
            nome,
            func.count(func.distinct(Orders.orderid)).label("quantidade_pedidos"),
            func.sum(OrderDetails.unitprice * OrderDetails.quantity).label("valor_vendas")
        ).join(Orders, Employees.employeeid == Orders.employeeid) \
         .join(OrderDetails, Orders.orderid == OrderDetails.orderid) \
         .filter(Orders.orderdate.between(inicio, fim)) \
         .group_by(nome) \
         .order_by(func.count(func.distinct(Orders.orderid)).desc()) \
         .all()

        return result
