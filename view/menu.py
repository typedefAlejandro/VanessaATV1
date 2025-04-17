from datetime import datetime
from controller.PedidosController import PedidosController
from controller.RelatoriosController import RelatoriosController

def view():
    
    while True:
        print("\nOlá! Você deseja realizar operações por meio do driver PSYCOPG ou pela ORM SQLALCHEMY?")
        print("Digite 1 para DRIVER - PSYCOPG \nDigite 2 para ORM - SQLALCHEMY \nDigite 3 para sair")
        operacao = int(input("Opção: "))
    
        match operacao:
            case 1:
                iniciarOperacoes("psycopg")
            case 2:
                iniciarOperacoes("alchemy")
            case _:
                exit()

def iniciarOperacoes(metodo):
    
    while True:
        print(f"\n[{metodo}] Você deseja inserir um pedido ou gerar relatórios?")
        print("Digite 1 para inserir pedidos \nDigite 2 para gerar relatórios \nDigite 3 para voltar")
        operacao = int(input("Opção: "))
    
        match operacao:
            case 1:
                iniciarInsercao(metodo)
            case 2:
                gerarRelatorios(metodo)
            case _:
                break
   
def iniciarInsercao(metodo):
    
    companyName = input("Company name (ex: Ernst Handel, Frankenversand): ")
    employeeName = input("Nome do vendedor (ex: Nancy Davolio, Andrew Fuller): ")
    productName = input("Nome do produto (ex: Chai, Tofu): ")
    quantity = int(input("Quantidade: "))
    unitPrice = float(input("Preço unitário: "))
    orderDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    if metodo == "psycopg":
        controllerPedidos = PedidosController()
        controllerPedidos.inserePedidoPsycopg(companyName, employeeName, productName, quantity, unitPrice, orderDate)    
    else:
        controllerPedidos = PedidosController()
        controllerPedidos.inserePedidoAlchemy(companyName, employeeName, productName, quantity, unitPrice, orderDate)    
    
def gerarRelatorios(metodo):
    
    while True:
        print(f"\n[{metodo}] Você deseja gerar relatórios de informações de pedido ou de ranking de funcionários por intervalo de tempo?")
        print("Digite 1 para relatórios de pedidos \nDigite 2 para relatórios de funcionários \nDigite 3 para voltar")
        operacao = int(input("Opção: "))
    
        match operacao:
            case 1:
                gerarRelatoriosPedidos(metodo)
            case 2:
                gerarRelatoriosFuncionarios(metodo)
            case _:
                break
    
def gerarRelatoriosPedidos(metodo):
    
    orderID = int(input("\nDigite a identificação do pedido a ser consultado: "))
    
    if metodo == "psycopg":
        controllerRelatorios = RelatoriosController()
        controllerRelatorios.gerarRelatoriosPedidosPsycopg(orderID)
    else:
        controllerRelatorios = RelatoriosController()
        controllerRelatorios.gerarRelatoriosPedidosAlchemy(orderID)
    
def gerarRelatoriosFuncionarios(metodo):
         
    while True:
        print(f"\n[{metodo}] Você deseja gerar relatórios evidenciando quantidade de vendas ou valor nominal total?")
        print("Digite 1 para relatórios de quantidades \nDigite 2 para relatórios de valor nominal \nDigite 3 para voltar")
        operacao = int(input("Opção: "))
   
        match operacao:
            case 1:
                gerarRelatoriosFuncionariosQuantidade(metodo)
            case 2:
                gerarRelatoriosFuncionariosValor(metodo)
            case _:
                break

def gerarRelatoriosFuncionariosQuantidade(metodo):
    
    inicio = input("Digite a data de início (formato YYYY-MM-DD): ")
    fim = input("Digite a data de fim (formato YYYY-MM-DD): ")
    datetime.strptime(inicio, "%Y-%m-%d")
    datetime.strptime(fim, "%Y-%m-%d")
    
    if metodo == "psycopg":       
        controllerRelatorios = RelatoriosController()
        controllerRelatorios.gerarRelatoriosFuncionariosQuantidadePsycopg(inicio, fim)
    else:
        controllerRelatorios = RelatoriosController()
        controllerRelatorios.gerarRelatoriosFuncionariosQuantidadeAlchemy(inicio, fim)
    
def gerarRelatoriosFuncionariosValor(metodo):
    inicio = input("Digite a data de início (formato YYYY-MM-DD): ")
    fim = input("Digite a data de fim (formato YYYY-MM-DD): ")
    datetime.strptime(inicio, "%Y-%m-%d")
    datetime.strptime(fim, "%Y-%m-%d")
    
    if metodo == "psycopg":       
        controllerRelatorios = RelatoriosController()
        controllerRelatorios.gerarRelatoriosFuncionariosValorPsycopg(inicio, fim)
    else:
        controllerRelatorios = RelatoriosController()
        controllerRelatorios.gerarRelatoriosFuncionariosValorAlchemy(inicio, fim)
    
    