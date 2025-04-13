import psycopg2
from DAO.OrdersDAO import OrdersDAO
from DAO.CustomersDAO import CustomersDAO
from DAO.EmployeesDAO import EmployeesDAO
from DAO.ProductsDAO import ProductsDAO
from DAO.OrderDetailsDAO import OrderDetailsDAO

class PedidosController:
    def inserePedido(self, companyName, employeeName, productName, quantity, unitPrice, orderDate):
        try:
            conn = psycopg2.connect(
            dbname="northwind",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432")
            cursor = conn.cursor()
            
            ordersDAO = OrdersDAO()
            customersDAO = CustomersDAO()
            employeesDAO = EmployeesDAO()
            productsDAO = ProductsDAO()
            orderDetailsDAO = OrderDetailsDAO()

            orderID = int(ordersDAO.retornaNovoIDInsercao(cursor))
            customerID = customersDAO.retornaIDPeloCompanyName(cursor, companyName)
            employeeID = int(employeesDAO.retornaIDpeloEmployeeName(cursor, employeeName))
            ordersDAO.inserePedido(cursor, orderID, customerID, employeeID, orderDate)
            
            productID = int(productsDAO.retornaIDPeloProductName(cursor, productName))
            orderDetailsDAO.insereDetalhesPedido(cursor, orderID, productID, unitPrice, quantity)
            
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"\nERRO AO INSERIR PEDIDO: {e}")
