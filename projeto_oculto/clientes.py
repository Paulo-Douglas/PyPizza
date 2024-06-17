import pickle
import textwrap
import os

################################################################
################################################################
##########                DICIONARIOS                 ##########
################################################################
################################################################

clientes = {}

################################################################
################################################################
##########                F U N Ç Õ E S               ##########
##########            S E C U N D A R I A S           ##########
################################################################
################################################################

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

def clear_screen():
    os.system('clear || cls')        

def get_name():
    while True:
        nome = input('Informe seu nome: ')
        if all(char.isalpha() or char.isspace() for char in nome):
            num_letras = sum(char.isalpha() for char in nome)
            if num_letras >= 4:
                return nome.title()
            else:
                print('O nome informado deve conter pelo menos 4 letras.')
        else:
            print('O nome informado é inválido. Informe um nome que possua somente letras e espaços!')

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

def verificar_cpf(cpf):
    return cpf in clientes

def get_cpf():
    verificar = True
    while verificar:
        cpf = input('Informe seu CPF: ')
        if not validar_cpf(cpf):
            print('O CPF informado não é válido. Por favor, informe um novo CPF.')
            continue
        if verificar_cpf(cpf):
            print('O CPF informado já está cadastrado no nosso sistema. Por favor, informe um novo CPF.')
            continue
        return cpf

def get_endereco():
    verificar = True
    while verificar:
        endereco = input('Informe seu endereço: ')
        return endereco.title()

def chamar_dados(cpf, clientes):
    nome = clientes[cpf][0]
    endereco = clientes[cpf][1]
    
    nome_quebrado = textwrap.fill(nome, width=45)
    endereco_quebrado = textwrap.fill(endereco, width=64)
    
    linhas_nome = nome_quebrado.split('\n')
    linhas_endereco = endereco_quebrado.split('\n')
    
    max_linhas = max(len(linhas_nome), len(linhas_endereco))
    for i in range(max_linhas):
        nome_final = linhas_nome[i] if i < len(linhas_nome) else ''
        endereco_final = linhas_endereco[i] if i < len(linhas_endereco) else ''
    return nome_final, endereco_final

def alt_decisao(cpf):
    alternativas = ['nome', 'cpf', 'endereço', 'endereco']
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    verificar = True
    while verificar:
        decisao = input('Qual dado você deseja alterar? - Tecle 0 caso não queira fazer alteração: ').lower()
        if decisao == '0':
            break
        elif decisao in alternativas:
            if decisao == 'nome':
                nome = get_name()
                clientes[cpf][0] = nome
                print('Nome alterado com sucesso.')
            elif decisao == 'cpf':
                novo_cpf = get_cpf()
                clientes[cpf] = novo_cpf
                print('O CPF foi alterado com sucesso.')
            else:
                endereco = get_endereco()
                clientes[cpf][1] = endereco
                print('O endereço foi alterado com sucesso.')
        else:
            print('Dado informado não existe. Escolha entre: NOME, CPF e ENDEREÇO.')
            continue
            
        resp = input('Deseja fazer uma nova alteração (sim/não) ? ').lower()
        if resp not in resposta:
            print('Resposta inválida. Responda com somente SIM ou NÃO.')
            continue
        if resp == 'n' or resp == 'nao' or resp == 'não':
            print('Alterações feitas com sucesso!!')
            verificar = False

def del_cliente(cpf):
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    verificar = True
    while verificar:
        resp = input('Caro cliente, realmente deseja excluir sua conta do sistema (sim/não)? ').lower()
        if resp not in resposta:
            print('Resposta inválida. Responda somente com SIM ou NÃO.')
            continue
        if resp in ['s', 'sim']:
            try:
                print('Exclusão bem-sucedida. Até mais.')
                del clientes[cpf]
            except KeyError:
                print('CPF não encontrado. Nenhuma exclusão realizada.')
                
        verificar = False


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

def cadastrar_clientes():
    clear_screen()
    print()
    print('----------------------------------------------')
    print('|                Cadastre - se               |')
    print('----------------------------------------------')
    print('|      Nome      |    CPF    |    Endereço   |')
    print('----------------------------------------------')
    print()
    nome = get_name()
    print()
    cpf = get_cpf()
    print()
    endereco = get_endereco()
    clientes[cpf] = [nome, endereco]
    print()
    print(f'Nome - {nome} | CPF - {cpf} | Endereço - {endereco}')
    print('Cadatro feito com sucesso!!')
    input('Tecle <ENTER> para continuar...')
    salvar_clientes()

def exibir_dados():
    clear_screen()
    print('----------------------------------------------')
    print('|                 Exibir Dados               |')
    print('----------------------------------------------')
    cpf = input('Informe seu cpf: ')
    if cpf in clientes:
        clear_screen()
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|                                                   Dados Cliente                                                                 |')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|                    Nome                     |       CPF       |                            Endereço                             |')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        nome = clientes[cpf][0]
        endereco = clientes[cpf][1]
        
        nome_quebrado = textwrap.fill(nome, width=45)
        endereco_quebrado = textwrap.fill(endereco, width=64)
        
        linhas_nome = nome_quebrado.split('\n')
        linhas_endereco = endereco_quebrado.split('\n')
        
        max_linhas = max(len(linhas_nome), len(linhas_endereco))
        for i in range(max_linhas):
            nome_final = linhas_nome[i] if i < len(linhas_nome) else ''
            endereco_final = linhas_endereco[i] if i < len(linhas_endereco) else ''
        print('|{:^45}'.format(nome_final), end='')
        print('|{:^17}'.format(cpf), end='')
        print('|{:^64}'.format(endereco_final), '|')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
    else:
        print('O cpf informado não está cadastrado no nosso sistema')
    print()
    input('Tecle <ENTER> para continuar...')

def alterar_dados():
    clear_screen()
    print('----------------------------------------------')
    print('|                Alterar Dados               |')
    print('----------------------------------------------')
    cpf = input('Informe seu cpf: ')
    if cpf in clientes:
        clear_screen()
        nome, endereco = chamar_dados(cpf, clientes)
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|                                                   Dados Cliente                                                                 |')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|                    Nome                     |       CPF       |                            Endereço                             |')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|{:^45}'.format(nome), end='')
        print('|{:^17}'.format(cpf), end='')
        print('|{:^64}'.format(endereco), '|')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        alt_decisao(cpf)
    else:
        print('O cpf informado não está cadastrado no nosso sistema.')

def excluir_cliente():
    clear_screen()
    print('----------------------------------------------')
    print('|                Excluir Cliente             |')
    print('----------------------------------------------')
    cpf = input('Informe seu cpf: ')
    if cpf in clientes:
        clear_screen()
        nome, endereco = chamar_dados(cpf, clientes)
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|                                                   Dados Cliente                                                                 |')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|                    Nome                     |       CPF       |                            Endereço                             |')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|{:^45}'.format(nome), end='')
        print('|{:^17}'.format(cpf), end='')
        print('|{:^64}'.format(endereco), '|')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        del_cliente(cpf)
    else:
        print('O cpf informado não está cadastrado no nosso sistema.')

################################################################
################################################################
##########    P R O G R A M A   P R I N C I P A L     ##########
################################################################
################################################################

carregar_clientes()

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

salvar_clientes()