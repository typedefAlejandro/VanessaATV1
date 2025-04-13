
class EmployeesDAO():
    def __init__(self):
        pass
        
    def retornaIDpeloEmployeeName(self, cursor, employeeName):
        query = f"""SELECT employeeid 
                FROM northwind.employees
                WHERE concat(firstname, ' ', lastname)
                LIKE '{employeeName}'"""
        cursor.execute(query)
        return cursor.fetchone()[0]

    def retornaSomaVendasFuncionarioPorIntervalo(self, cursor, inicio, fim):
        query = f"""SELECT concat(e.firstname ,' ' ,  e.lastname) as name, 
                    count(distinct(o.orderid)) as quantidade_pedidos, 
                    sum(od.unitprice * od.quantity) as valor_vendas
                    FROM northwind.orders o 
                    JOIN northwind.employees e 
                        ON o.employeeid = e.employeeid
                    JOIN northwind.order_details od 
                        ON o.orderid = od.orderid
                    WHERE o.orderdate BETWEEN '{inicio}' AND '{fim}'
                    GROUP BY name
                    order by valor_vendas desc"""
        cursor.execute(query)
        return cursor.fetchall()

    def retornaSomaPedidosFuncionarioPorIntervalo(self, cursor, inicio, fim):
        query = f"""SELECT concat(e.firstname ,' ' ,  e.lastname) as name, 
                    count(distinct(o.orderid)) as quantidade_pedidos, 
                    sum(od.unitprice * od.quantity) as valor_vendas
                    FROM northwind.orders o 
                    JOIN northwind.employees e 
                        ON o.employeeid = e.employeeid
                    JOIN northwind.order_details od 
                        ON o.orderid = od.orderid
                    WHERE o.orderdate BETWEEN '{inicio}' AND '{fim}'
                    GROUP BY name
                    order by quantidade_pedidos desc"""
        cursor.execute(query)
        return cursor.fetchall()