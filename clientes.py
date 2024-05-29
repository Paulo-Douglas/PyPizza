import pickle
import os

def carregar_clientes():
    clientes = {}
    try:
        arq_clientes = open("clientes.dat", "rb")
        clientes = pickle.load(arq_clientes)
        return clientes
    except:
        arq_clientes = open("clientes.dat", "wb")
        arq_clientes.close()

clientes = carregar_clientes()

################################################################
################################################################
##########                F U N Ç Õ E S               ########## 
##########            S E C U N D A R I A S           ##########
################################################################
################################################################
def clear_screen():
    os.system('clear || cls')

def cadastrar_cliente():
    clientes = {}
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

################################################################
################################################################
##########               F U N Ç Õ E S                ##########
################################################################
################################################################

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