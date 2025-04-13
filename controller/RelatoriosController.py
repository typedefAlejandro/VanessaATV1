import psycopg2
from DAO.OrdersDAO import OrdersDAO
from DAO.CustomersDAO import CustomersDAO
from DAO.EmployeesDAO import EmployeesDAO
from DAO.ProductsDAO import ProductsDAO
from DAO.OrderDetailsDAO import OrderDetailsDAO

class RelatoriosController():

    def gerarRelatoriosPedidos(self, orderID):
        try:
            conn = psycopg2.connect(
            dbname="northwind",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432")
            cursor = conn.cursor()
            
            ordersDAO = OrdersDAO()
            data = ordersDAO.retornaRelatorioPedido(cursor, orderID)
            
            self.imprimirRelatorioPedidos(data)

            cursor.close()
            conn.close()
        except Exception as e:
            print(f"\nERRO AO CONSULTAR PEDIDO: {e}")     
            
    def imprimirRelatorioPedidos(self, relatorio):
        if not relatorio:
            print("\nNenhum pedido encontrado.\n")
            return

        print("\n===== RELATÓRIO DO PEDIDO =====")
        print(f"Pedido ID: {relatorio[0][0]}")
        print(f"Data do Pedido: {relatorio[0][1]}")
        print(f"Cliente: {relatorio[0][2]}")
        print(f"Funcionário: {relatorio[0][3]}")
        print("\nProdutos:")
        print("-" * 50)
        print(f"{'Produto':<25} {'Qtd':<5} {'Preço Unit.':<10}")
        print("-" * 50)

        for linha in relatorio:
            produto = linha[4]
            quantidade = linha[5]
            preco_unitario = linha[6]
            print(f"{produto:<25} {quantidade:<5} {preco_unitario:<10.2f}")
        
        print("-" * 50)
        
    def gerarRelatoriosFuncionariosValor(self, inicio, fim):
        try:
            conn = psycopg2.connect(
            dbname="northwind",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432")
            cursor = conn.cursor()
            
            employeesDAO = EmployeesDAO()
            data = employeesDAO.retornaSomaVendasFuncionarioPorIntervalo(cursor, inicio, fim)
            
            self.imprimirRelatorioFuncionarios(data, inicio, fim)

            cursor.close()
            conn.close()
        except Exception as e:
            print(f"\nERRO AO CONSULTAR PEDIDO: {e}")
    
    def gerarRelatoriosFuncionariosQuantidade(self, inicio, fim):
        try:
            conn = psycopg2.connect(
            dbname="northwind",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432")
            cursor = conn.cursor()
            
            employeesDAO = EmployeesDAO()
            data = employeesDAO.retornaSomaPedidosFuncionarioPorIntervalo(cursor, inicio, fim)
            
            self.imprimirRelatorioFuncionarios(data, inicio, fim)

            cursor.close()
            conn.close()
        except Exception as e:
            print(f"\nERRO AO CONSULTAR PEDIDO: {e}")

    def imprimirRelatorioFuncionarios(self, relatorio, inicio, fim):
        if not relatorio:
            print("Nenhum dado encontrado para o intervalo.")
            return

        print(f"\n===== RELATÓRIO DE VENDAS POR FUNCIONÁRIO =====")
        print(f"Período: {inicio} até {fim}")
        print("-" * 60)
        print(f"{'Funcionário':<25} {'Pedidos':<10} {'Total Vendido':<15}")
        print("-" * 60)

        for linha in relatorio:
            nome = linha[0]
            quantidade = linha[1]
            total = linha[2]
            print(f"{nome:<25} {quantidade:<10} R$ {total:<15.2f}")

        print("-" * 60)
