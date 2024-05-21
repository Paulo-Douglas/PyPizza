import pickle
import os

################################################################
################################################################
##########                DICIONARIOS                 ##########
################################################################
################################################################

clientes = {}
try:
    arq_clientes = open("clientes.dat", "rb")
    clientes = pickle.load(arq_clientes)
except:
    arq_clientes = open("clientes", "wb")
    arq_clientes.close()

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
            "média": 23.00,
            "grande": 27.00,
            "família": 29.00
        },
        "margherita": {
            "pequena": 25.00,
            "média": 23.00,
            "grande": 27.00,
            "família": 29.00
        },
        "quatro queijos": {
            "pequena": 25.00,
            "média": 23.00,
            "grande": 27.00,
            "família": 29.00
        },
        "frango com catupiry": {
            "pequena": 25.00,
            "média": 23.00,
            "grande": 27.00,
            "família": 29.00
        },
        "calabresa": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "portuguesa": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "vegetariana": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "carne seca com rúcula": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "chocolate": {
            "pequena": 20.00,
            "média": 21.00,
            "grande": 22.00,
            "família": 24.00
        },
        "morango com nutella": {
            "pequena": 20.00,
            "média": 21.00,
            "grande": 22.00,
            "família": 24.00
        },
        "banana com canela": {
            "pequena": 20.00,
            "média": 21.00,
            "grande": 22.00,
            "família": 24.00
        },
        "romeu e julieta": {
            "pequena": 20.00,
            "média": 21.00,
            "grande": 22.00,
            "família": 24.00
        }
    }

################################################################
################################################################
##########                F U N Ç Õ E S               ########## 
##########            S E C U N D A R I A S           ##########
################################################################
################################################################

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
    print('|             2 - Login                      |')
    print('|             3 - Exibir Dados               |')
    print('|             4 - Alterar Dados              |')
    print('|             5 - Excluir Cliente            |')
    print('|             0 - Retornar ao Menu Principal |')
    print('----------------------------------------------')
    op_cliente = input("Escolha sua opção: ")
    return op_cliente