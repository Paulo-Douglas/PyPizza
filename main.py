import módulo.utils  as ut
import os

clientes = {}
cardapio = {
    "pizzas salgadas": {
        "pequena": 23.00,
        "média": 25.00,
        "grande": 27.00,
        "família": 29.00
    }, 
    "pizzas especiais": {
        "pequena": 28.00,
        "média": 30.00,
        "grande": 32.00,
        "família": 35.00
    },
    "pizzas doces": {
        "pequena": 20.00,
        "média": 21.00,
        "grande": 22.00,
        "família": 24.00
    }
}
funcionarios = {}

################################################################
################################################################
##########               F U N Ç Õ E S                ##########
################################################################
################################################################

def menu_principal():
    os.system('clear')
    print('----------------------------------------------')
    print('|         Sistema de Gestão - Pizzaria       |')
    print('----------------------------------------------')
    print('|             1 - Clientes                   |')
    print('|             2 - Pedidos                    |')
    print('|             3 - Funcionários               |')
    print('|             4 - Administração              |')
    print('|             5 - Sobre a Pizzaria           |')
    print('|             0 - Sair                       |')
    print('----------------------------------------------')
    op_prin = input("Escolha sua opção: ")
    return op_prin

def menu_clientes():
    os.system('clear')
    print()
    print('----------------------------------------------')
    print('|                  Clientes                  |')
    print('----------------------------------------------')
    print('|             1 - Cadastre - se              |')
    print('|             2 - Exibir Dados               |')
    print('|             3 - Alterar Dados              |')
    print('|             4 - Excluir Cliente            |')
    print('|             0 - Retornar ao Menu Principal |')
    print('----------------------------------------------')
    op_cliente = input("Escolha sua opção: ")
    return op_cliente

def cadatrar_clientes():
    os.system('clear')
    print()
    print('----------------------------------------------')
    print('|                 Cadastre - se              |')
    print('----------------------------------------------')
    print('| Nome   | Telefone   | Email   | Endereço   |')
    print('----------------------------------------------')
    print()
    nome = input('Nome: ')
    print()
    fone = input('Telefone: ')
    while not ut.validar_numero(fone):
        fone = input('Telefone: ')
    print()
    email = input('Email: ')
    while not ut.validar_email(email):
        print("Por favor, insira um email válido.")
        email = input('Email: ')
    print()
    endereco = input('Endereço: ')
    print()
    clientes[email] = [nome, fone, endereco]
    print()
    print(clientes)
    print('Cadatro feito com sucesso!!')
    input('Tecle <ENTER> para continuar...')

def exibir_dados():
    os.system('clear')
    print()
    print('----------------------------------------------')
    print('|                 Exibir Dados               |')
    print('----------------------------------------------')
    print('| Nome   | Telefone   | Email   | Endereço   |')
    print('----------------------------------------------')
    email = input('Informe o seu email: ')
    if email in clientes:
        print('Nome: ', clientes[email][0])
        print('Telefone: ', clientes[email][1])
        print('Email: ', email)
        print('Endereço: ', clientes[email][2])
    else:
        print('O email informado é inexistencia')
    print()
    input('Tecle <ENTER> para continuar...')

def alterar_dados():
    os.system('clear')
    print()
    print('----------------------------------------------')
    print('|                 Alterar Dados              |')
    print('----------------------------------------------')
    print('| Nome   | Telefone   | Email   | Endereço   |')
    print('----------------------------------------------')
    email = input('Informe o seu email: ')
    if email in clientes:
        nome = input('Nome: ')
        print()
        fone = input('Telefone: ')
        print()
        endereco = input('Endereço: ')
        clientes[email] = [nome, fone, endereco]
    else:
        print('O email é inexistente')
    print('Dados alterados com sucesso!!')
    input('Tecle <ENTER> para combinar...')

def excluir_cliente():
    os.system('clear')
    print('----------------------------------------------')
    print('|                Excluir Cliente             |')
    print('----------------------------------------------')
    email = input('Email: ')
    if email in clientes:
        del clientes[email]
    else:
        print('O email informado é inexistente')
        print()
    print('Cliente excluido com sucesso!!')
    input('Tecle <ENTER> para combinar...')

def menu_pedidos():
    os.system('clear')
    print()
    print('----------------------------------------------')
    print('|                   Pedidos                  |')
    print('----------------------------------------------')
    print('|             1 - Cardápio                   |')
    print('|             2 - Carrinho                   |')
    print('|             3 - Promoções                  |')
    print('|             0 - Retornar ao Menu Principal |')
    print('----------------------------------------------')
    op_pedidos = input("Escolha sua opção: ")
    return op_pedidos

def menu():
    os.system('clear')
    print()
    print('-------------------------------------------------')
    print('|                    Cardápio                   |')
    print('-------------------------------------------------')
    print('|                Pizzas Salgadas                |')
    print('|-----------------------------------------------|')
    print(f'| 1. Pepperoni           | R$ {cardapio["pizzas salgadas"]["pequena"]:.2f} - Pequena   |')
    print(f'| 2. Margherita          | R$ {cardapio["pizzas salgadas"]["média"]:.2f} - Média     |')
    print(f'| 3. Quatro Queijos      | R$ {cardapio["pizzas salgadas"]["grande"]:.2f} - Grande    |')
    print(f'| 4. Frango com Catupiry | R$ {cardapio["pizzas salgadas"]["família"]:.2f} - Família   |')
    print('|-----------------------------------------------|')
    print('|                Pizzas Especiais               |')
    print('|-----------------------------------------------|')
    print(f'| 5. Calabresa             | R$ {cardapio["pizzas especiais"]["pequena"]:.2f} - Pequena |')
    print(f'| 6. Portuguesa            | R$ {cardapio["pizzas especiais"]["média"]:.2f} - Média   |')
    print(f'| 7. Vegetariana           | R$ {cardapio["pizzas especiais"]["grande"]:.2f} - Grande  |')
    print(f'| 8. Carne Seca com Rúcula | R$ {cardapio["pizzas especiais"]["família"]:.2f} - Família |')
    print('|-----------------------------------------------|')
    print('|                  Pizzas Doces                 |')
    print('|-----------------------------------------------|')
    print(f'| 9. Chocolate           | R$ {cardapio["pizzas doces"]["pequena"]:.2f} - Pequena   |')
    print(f'|10. Morango com Nutella | R$ {cardapio["pizzas doces"]["média"]:.2f} - Média     |')
    print(f'|11. Banana com Canela   | R$ {cardapio["pizzas doces"]["grande"]:.2f} - Grande    |')
    print(f'|12. Romeu e Julieta     | R$ {cardapio["pizzas doces"]["família"]:.2f} - Família   |')
    print('|-----------------------------------------------|')
    print('|              Tamanhos Disponíveis             |')
    print('|-----------------------------------------------|')
    print('| Pequena - 6 fatias  | Média - 8 fatias        |')
    print('| Grande - 10 fatias  | Família - 12 fatias     |')
    print('|-----------------------------------------------|')
    print('|          0 - Retornar ao Menu Principal       |')
    print('-------------------------------------------------')
    ut.fazer_pedido()

def cesto():
    os.system('clear')
    print()
    print('----------------------------------------------')
    print('|                  Carrinho                  |')
    print('----------------------------------------------')
    ut.imprimir_recibo()

def menu_funcionario():
    os.system('clear')
    print('----------------------------------------------')
    print('|                Funcionários                |')
    print('----------------------------------------------')
    print('|             1 - Login                      |')
    print('|             2 - Controle de Pedidos        |')
    print('|             3 - Estoque                    |')
    print('|             0 - Retornar ao Menu Principal |')
    print('----------------------------------------------')
    op_funcio = input('Escolha sua opção: ')
    return op_funcio

def login():
    print('----------------------------------------------')
    print('|                Funcionários                |')
    print('----------------------------------------------')
    print('| Email         | Senha         | Código     |')
    print('----------------------------------------------')
    email = input('Informe seu email: ')
    while not ut.validar_email(email):
        print("Por favor, insira um email válido.")
        email = input('Email: ')
    senha = input('Informe sua senha: ')
    print()
    codigo = input('Informe seu código de acesso: ')
    print()
    clientes[email] = [senha, codigo]

def administracao():
    print()
    print('----------------------------------------------')
    print('|                Administração               |')
    print('----------------------------------------------')
    print('|             1 - Relatório de Vendas        |')
    print('|             2 - Despesas                   |')
    print('|             3 - Gestão Geral               |')
    print('|             0 - Retornar ao Menu Principal |')
    print('----------------------------------------------')
    print()
    op_adm = input("Escolha sua opção: ")

def pizzaria():
    print()
    print('----------------------------------------------')
    print('|            Sobre a Pizzaria                |')
    print('----------------------------------------------')
    print('| Projeto de Gestão de Pizzaria.             |')
    print('| Desenvolvido por: Paulo Douglas.           |')
    print('| Email: paulo.martins.132@ufrn.edu.com      |')
    print('| GitHub: Paulo-Douglas                      |')
    print('----------------------------------------------')
    input("Tecle <ENTER> para continuar...")

################################################################
################################################################
##########    P R O G R A M A   P R I N C I P A L     ##########
################################################################
################################################################

op_prin = ''
while op_prin != '0':
    op_prin = menu_principal()  # Aqui deve ser chamado menu_principal(), não menu_clientes()
    
    if op_prin == '1':
        op_cliente = ''
        while op_cliente != '0':
            op_cliente = menu_clientes()
            if op_cliente == '1':
                cadatrar_clientes()
            elif op_cliente == '2':
                exibir_dados()
            elif op_cliente == '3':
                alterar_dados()
            elif op_cliente =='4':
                excluir_cliente
                
    elif op_prin == '2':
        op_pedidos = ''
        while op_pedidos != '0':
            op_pedidos = menu_pedidos()
            if op_pedidos == '1':
                menu()
            elif op_pedidos == '2':
                cesto()
    
    elif op_prin == '4':
        op_adm = ''
        while op_adm != '0':
            op_adm = administracao()
    
    elif op_prin == '5':
        pizzaria()