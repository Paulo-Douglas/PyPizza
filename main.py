import pickle
import textwrap
import os

################################################################
################################################################
##########                DICIONARIOS                 ##########
################################################################
################################################################

clientes = {}

carrinho = {}
try:
    arq_carrinho = open("carrinho.dat", "rb")
    carrinho = pickle.load(arq_carrinho)
except:
    arq_carrinho = open("carrinho.dat", "wb")
    arq_carrinho.close()

funcionarios = {}

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

menu_pizzas = {
        "pepperoni": {
            "pequena": cardapio["pizzas salgadas"]["pequena"],
            "média": cardapio["pizzas salgadas"]["média"],
            "grande": cardapio["pizzas salgadas"]["grande"],
            "família": cardapio["pizzas salgadas"]["família"]
        },
        "margherita": {
            "pequena": cardapio["pizzas salgadas"]["pequena"],
            "média": cardapio["pizzas salgadas"]["média"],
            "grande": cardapio["pizzas salgadas"]["grande"],
            "família": cardapio["pizzas salgadas"]["família"]
        },
        "quatro queijos": {
            "pequena": cardapio["pizzas salgadas"]["pequena"],
            "média": cardapio["pizzas salgadas"]["média"],
            "grande": cardapio["pizzas salgadas"]["grande"],
            "família": cardapio["pizzas salgadas"]["família"]
        },
        "frango com catupiry": {
            "pequena": cardapio["pizzas salgadas"]["pequena"],
            "média": cardapio["pizzas salgadas"]["média"],
            "grande": cardapio["pizzas salgadas"]["grande"],
            "família": cardapio["pizzas salgadas"]["família"]
        },
        "calabresa": {
            "pequena": cardapio["pizzas especiais"]["pequena"],
            "média": cardapio["pizzas especiais"]["média"],
            "grande": cardapio["pizzas especiais"]["grande"],
            "família": cardapio["pizzas especiais"]["família"]
        },
        "portuguesa": {
            "pequena": cardapio["pizzas especiais"]["pequena"],
            "média": cardapio["pizzas especiais"]["média"],
            "grande": cardapio["pizzas especiais"]["grande"],
            "família": cardapio["pizzas especiais"]["família"]
        },
        "vegetariana": {
            "pequena": cardapio["pizzas especiais"]["pequena"],
            "média": cardapio["pizzas especiais"]["média"],
            "grande": cardapio["pizzas especiais"]["grande"],
            "família": cardapio["pizzas especiais"]["família"]
        },
        "carne seca com rúcula": {
            "pequena": cardapio["pizzas especiais"]["pequena"],
            "média": cardapio["pizzas especiais"]["média"],
            "grande": cardapio["pizzas especiais"]["grande"],
            "família": cardapio["pizzas especiais"]["família"]
        },
        "chocolate": {
            "pequena": cardapio["pizzas doces"]["pequena"],
            "média": cardapio["pizzas doces"]["média"],
            "grande": cardapio["pizzas doces"]["grande"],
            "família": cardapio["pizzas doces"]["família"]
        },
        "morango com nutella": {
            "pequena": cardapio["pizzas doces"]["pequena"],
            "média": cardapio["pizzas doces"]["média"],
            "grande": cardapio["pizzas doces"]["grande"],
            "família": cardapio["pizzas doces"]["família"]
        },
        "banana com canela": {
            "pequena": cardapio["pizzas doces"]["pequena"],
            "média": cardapio["pizzas doces"]["média"],
            "grande": cardapio["pizzas doces"]["grande"],
            "família": cardapio["pizzas doces"]["família"]
        },
        "romeu e julieta": {
            "pequena": cardapio["pizzas doces"]["pequena"],
            "média": cardapio["pizzas doces"]["média"],
            "grande": cardapio["pizzas doces"]["grande"],
            "família": cardapio["pizzas doces"]["família"]
        }
    }

################################################################
################################################################
##########                F U N Ç Õ E S               ########## 
##########            S E C U N D A R I A S           ##########
################################################################
################################################################

def clear_screen():
    os.system('clear || cls')

def carregar_clientes():
    global clientes
    try:
        arq_clientes = open("clientes.dat", "rb")
        clientes = pickle.load(arq_clientes)
    except (FileNotFoundError, EOFError):
        arq_clientes = open("clientes.dat", "wb")
        pickle.dump(clientes, arq_clientes)

def salvar_clientes():
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    soma = 0
    for indice in range(9):
        soma += int(cpf[indice]) * (10 - indice)
    resto = soma % 11
    if resto < 2:
        digito_verificador1 = 0
    else:
        digito_verificador1 = 11 - resto
    if digito_verificador1 != int(cpf[9]):
        return False
    soma2 = 0
    for indice in range(10):
        soma2 += int(cpf[indice]) * (11 - indice)
    resto2 = soma2 % 11
    if resto2 < 2:
        digito_verificador2 = 0
    else:
        digito_verificador2 = 11 - resto2
    if digito_verificador2 != int(cpf[10]):
        return False
    return True

def verificar_clientes(cpf):
    verificar = True
    while verificar:
        if not validar_cpf(cpf):
            print('CPF informado é inválido. Por Favor, informe outro')
            cpf = input('Informe o CPF: ')
        else:
            clientes = carregar_clientes()
            if cpf in clientes:
                verificar = False
            else:
                print('Cliente não encontrado, cadastre-se!')
                verificar = True

def validar_opcao(opcao, menu_pizzas):
    if opcao == '0':
        return False
    if opcao not in menu_pizzas:
        print('Nome da pizza inválido. Por favor, informe uma pizza do nosso cardápio.')
        return False
    return True

def validar_tamanho(opcao, tamanho, menu_pizzas):
    pizza_escolhida = menu_pizzas[opcao]
    if tamanho not in pizza_escolhida:
        print('Tamanho de pizza inválido. Por favor, informe um tamanho válido.')
        return False
    return True

def obter_preco(opcao, tamanho, menu_pizzas):
    pizza_escolhida = menu_pizzas[opcao]
    return pizza_escolhida[tamanho]

def adicionar_carrinho(cpf, opcao, tamanho, preco_pizza, carrinho):
    carrinho[cpf] = [opcao, tamanho, preco_pizza]
    arq_carrinho = open("carrinho.dat", "wb")
    pickle.dump(carrinho, arq_carrinho)
    arq_carrinho.close()

def imprimir_recibo():
    cpf = input('Caro cliente, informe seu CPF: ')
    if validar_cpf(cpf):
        if verificar_clientes(cpf):
            try:
                with open("carrinho.dat", "rb") as arq_carrinho:
                    carrinho = pickle.load(arq_carrinho)
                    if cpf in carrinho:
                        print('Esse foi seu pedido:')
                        for item in carrinho[cpf]:
                            print(f'Pizza: {item[0]}, Tamanho: {item[1]}, Preço: R$ {item[2]:.2f}')
                    else:
                        print('Nenhum pedido encontrado para este CPF.')
            except (FileNotFoundError, EOFError):
                print('Nenhum pedido encontrado.')
        else:
            print('CPF não cadastrado.')
    else:
        print('CPF inválido.')

def fazer_pedido():
    cpf = input('Caro cliente, para continuar digite seu cpf: ')
    if verificar_clientes(cpf):
        verificar = True
        while verificar:
            opcao = input('Caro cliente, informe o nome da pizza desejada (ou 0 para sair): ').lower()
            if opcao == '0':
                return
            if not validar_opcao(opcao, menu_pizzas):
                continue
            tamanho = input('Informe o tamanho da sua pizza (pequena/média/grande/família): ').lower()
            if not validar_tamanho(opcao, tamanho, menu_pizzas):
                continue
            preco_pizza = obter_preco(opcao, tamanho, menu_pizzas)
            adicionar_carrinho(cpf, opcao, tamanho, preco_pizza, carrinho)
            adicionar_outra = input("Você deseja adicionar outra pizza ao carrinho? (sim/não): ").lower()
            if adicionar_outra != 'sim':
                verificar = False
    else:
        print('CPF não cadrastado, cadraste - se e faça seu pedido!')

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
    clear_screen()
    print()
    print('----------------------------------------------')
    print('|                  Clientes                  |')
    print('----------------------------------------------')
    print('|             1 - Cadastre - se              |')
    print('|             3 - Exibir Dados               |')
    print('|             4 - Alterar Dados              |')
    print('|             5 - Excluir Cliente            |')
    print('|             0 - Retornar ao Menu Principal |')
    print('----------------------------------------------')
    op_cliente = input("Escolha sua opção: ")
    return op_cliente

def cadastrar_clientes():
    clear_screen()
    print()
    print('----------------------------------------------')
    print('|                Cadastre - se               |')
    print('----------------------------------------------')
    print('| Nome   | CPF     | Senha   | Endereço      |')
    print('----------------------------------------------')
    print()
    nome = input('Nome: ')
    print()
    cpf = input('CPF: ')
    while not validar_cpf(cpf):
        print("Por favor, insira um cpf válido.")
        cpf = input('CPF: ')
    print()
    senha = input('Senha: ')
    print()
    endereco = input('Endereço: ')
    print()
    cliente = clientes[cpf] = [nome, senha, endereco]
    cadastrar_cliente(cliente)
    print(f'Nome - {nome} | CPF - {cpf} | Senha - {senha} | Endereço - {endereco}')
    print('Cadatro feito com sucesso!!')
    input('Tecle <ENTER> para continuar...')

def exibir_dados():
    clear_screen()
    print('----------------------------------------------')
    print('|                 Exibir Dados               |')
    print('----------------------------------------------')
    print('| Nome   | CPF     | Senha   | Endereço      |')
    print('----------------------------------------------')
    cpf = input('Informe o seu CPF: ')
    if cpf in clientes:
        print('Nome: ', clientes[cpf][0])
        print('Email: ', cpf)
        print('Senha: ', clientes[cpf][1])
        print('Endereço: ', clientes[cpf][2])
    else:
        print('O cpf informado é inexistencia')
    print()
    input('Tecle <ENTER> para continuar...')

def alterar_dados():
    clear_screen()
    print()
    print('----------------------------------------------')
    print('|                 Alterar Dados              |')
    print('----------------------------------------------')
    print('| Nome   | CPF     | Senha   | Endereço      |')
    print('----------------------------------------------')
    cpf = input('Informe o seu email: ')
    if cpf in clientes:
        nome = input('Nome: ')
        print()
        senha = input('Senha: ')
        print()
        endereco = input('Endereço: ')
        clientes[cpf] = [nome, senha, endereco]
    else:
        print('O cpf é inexistente')
    print('Dados alterados com sucesso!!')
    input('Tecle <ENTER> para continuar...')

def excluir_cliente():
    clear_screen()
    print('----------------------------------------------')
    print('|                Excluir Cliente             |')
    print('----------------------------------------------')
    cpf = input('Cpf: ')
    if cpf in clientes:
        del clientes[cpf]
    else:
        print('O cpf informado é inexistente')
        print()
    print('Cliente excluido com sucesso!!')
    input('Tecle <ENTER> para combinar...')

def menu_pedidos():
    os.system('clear')
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
    fazer_pedido()

def cesto():
    os.system('clear')
    print()
    print('----------------------------------------------')
    print('|                  Carrinho                  |')
    print('----------------------------------------------')
    imprimir_recibo()

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

def login_fucionarios():
    print('----------------------------------------------')
    print('|                Funcionários                |')
    print('----------------------------------------------')
    print('| Email         | Senha         | Código     |')
    print('----------------------------------------------')

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
    return op_adm

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
                cadastrar_clientes()
            elif op_cliente == '2':
                exibir_dados()
            elif op_cliente == '3':
                alterar_dados()
            elif op_cliente =='4':
                excluir_cliente()

    elif op_prin == '2':
        op_pedidos = ''
        while op_pedidos != '0':
            op_pedidos = menu_pedidos()
            if op_pedidos == '1':
                menu()
            elif op_pedidos == '2':
                cesto()
            elif op_pedidos == '3':
                print('oi')
    
    elif op_prin == '4':
        op_adm = ''
        while op_adm != '0':
            op_adm = administracao()
    
    elif op_prin == '5':
        pizzaria()

