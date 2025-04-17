import psycopg2
from DAO.OrdersDAO import OrdersDAO
from DAO.CustomersDAO import CustomersDAO
from DAO.EmployeesDAO import EmployeesDAO
from DAO.ProductsDAO import ProductsDAO
from DAO.OrderDetailsDAO import OrderDetailsDAO
from DAO.OrdersDAOORM import OrdersDAOORM
from DAO.CustomersDAOORM import CustomersDAOORM
from DAO.EmployeesDAOORM import EmployeesDAOORM
from DAO.ProductsDAOORM import ProductsDAOORM
from dbConfig import SessionLocal

class PedidosController:
    def inserePedidoPsycopg(self, companyName, employeeName, productName, quantity, unitPrice, orderDate):
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
            employeeID = employeesDAO.retornaIDpeloEmployeeName(cursor, employeeName)

            if not customerID:
                print("\nCliente não encontrado.")
                return
            if not employeeID:
                print("\nFuncionário não encontrado.")
                return

            ordersDAO.inserePedido(cursor, orderID, customerID, int(employeeID), orderDate)

            productID = productsDAO.retornaIDPeloProductName(cursor, productName)
            if not productID:
                print("\nProduto não encontrado.")
                return

            orderDetailsDAO.insereDetalhesPedido(cursor, orderID, int(productID), unitPrice, quantity)

            conn.commit()
            cursor.close()
            conn.close()
            print("\nPedido inserido com sucesso (DRIVER).")
        except Exception as e:
            print(f"\nERRO AO INSERIR PEDIDO (DRIVER): {e}")


    def inserePedidoAlchemy(self, companyName, employeeName, productName, quantity, unitPrice, orderDate):
        try:
            session = SessionLocal()

            customersDAO = CustomersDAOORM(session)
            employeesDAO = EmployeesDAOORM(session)
            productsDAO = ProductsDAOORM(session)
            ordersDAO = OrdersDAOORM(session)

            orderID = ordersDAO.retornaNovoIDInsercao()
            customerID = customersDAO.retornaIDPeloCompanyName(companyName)
            employeeID = employeesDAO.retornaIDpeloEmployeeName(employeeName)
            productID = productsDAO.retornaIDPeloProductName(productName)

            if not customerID:
                print("\nCliente não encontrado.")
                return
            if not employeeID:
                print("\nFuncionário não encontrado.")
                return
            if not productID:
                print("\nProduto não encontrado.")
                return

            ordersDAO.inserePedidoComDetalhes(
                order_id=orderID,
                customer_id=customerID,
                employee_id=employeeID,
                order_date=orderDate,
                details=[
                    {
                        "product_id": productID,
                        "quantity": quantity,
                        "unit_price": unitPrice
                    }
                ]
            )

            session.commit()
            print("\nPedido inserido com sucesso (ORM).")

        except Exception as e:
            session.rollback()
            print(f"\nERRO AO INSERIR PEDIDO (ORM): {e}")
        finally:
            session.close()
