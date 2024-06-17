import textwrap
import random
import pickle
import os

################################################################
################################################################
##########                DICIONARIOS                 ##########
################################################################
################################################################

clientes = {}
cardapio = {}
carrinho = {}

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

def carregar_cardapio():
    global cardapio
    try:
        arq_cardapio = open("cardapio.dat", "rb")
        cardapio = pickle.load(arq_cardapio)
    except (FileNotFoundError, EOFError):
        arq_cardapio = open("cardapio.dat", "wb")
        pickle.dump(cardapio, arq_cardapio)

def salvar_cardapio():
    arq_cardapio = open("cardapio.dat", "wb")
    pickle.dump(cardapio, arq_cardapio)
    arq_cardapio.close()

def nome_pizza(cardapio):
    while True:
        nome = input('Informe o nome da pizza: ').title()
        if all(char.isalpha() or char.isspace() for char in nome):
            if any(nome == detalhes[0] for detalhes in cardapio.values()):
                print('Essa pizza já está cadastrada no cardápio. Por favor, informe uma nova pizza.')
                continue
            else:
                num_letras = sum(char.isalpha() for char in nome)
                if num_letras >= 4:
                    return nome.title()
                else:
                    print('O nome informado deve conter pelo menos 4 letras.')
        else:
            print('O nome de pizza informado é inválido. Informe um que possua somente letras e espaços!')

def get_ingredientes():
    ingredientes = []
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    verificar = True
    while verificar:
        ing = input('Digite o nome do ingrediente que você deseja adicionar: ').title()
        if all(char.isalpha() or char.isspace() for char in ing):
            num_letras = sum(char.isalpha() for char in ing)
            if num_letras >= 5:
                ingredientes.append(ing)
                print(*ingredientes, sep = ' - ')
            else:
                print('O ingrediente informado deve ter no mínimo 4 letras.')
        else:
            print('O ingrediente informado é inválido. Informe um que possua somente letras e espaços.')
            
        resp = input('Deseja adicionar mais ingredientes (sim/não) ? ').lower()
        if resp not in alternativas:
            print('A resposta é inválida. Por favor, escolha entre SIM ou NÃO')
            continue
        if resp == 'n' or resp == 'nao' or resp == 'não':
            print('Ingrediente(s) foram adicionados com sucesso.')
            break
    return ingredientes

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def valor_pizza():
    valores = []
    while True:
        valorP = input('Digite o valor da pizza tamanho P: ')
        valorM = input('Digite o valor da pizza tamanho M: ')
        valorG = input('Digite o valor da pizza tamanho G: ')
        valorGG = input('Digite o valor da pizza tamanho GG: ')
        
        valores.append(valorP)
        valores.append(valorM)
        valores.append(valorG)
        valores.append(valorGG)
        return valores

# def fazer_pedido(cpf, valores):
#     tamanhos = ['p', 'm', 'g', 'gg']
#     while True:
#         id = input('Informe o ID da pizza: ')
#         if id in cardapio:
#             tamanho = input('Informe o tamanho da pizza (P/M/G/GG): ').lower()
#             if tamanho in tamanhos:
#                 float(valores)
#                 match tamanho:
#                     case 'p':
#                         valores[0] = 'p'
#                     case 'm':
#                         valores[1] = 'm'
#                     case 'g':
#                         valores[2] = 'g'
#                     case 'gg':
#                         valores[3] = 'gg'
#                 pedido = f''
#             else:
#                 print('O tamanho informado é inválido. Por favor, informe (P/M/G/GG).')

################################################################
################################################################
##########               F U N Ç Õ E S                ##########
################################################################
################################################################

def menu_principal():
    clear_screen()
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

def menu_pedidos():
    clear_screen()
    print('----------------------------------------------')
    print('|                  Cardápio                  |')
    print('----------------------------------------------')
    print('|             1 - Menu                       |')
    print('|             2 - Carrinho                   |')
    print('|             3 - Promoções                  |')
    print('|             4 - Cadastrar Pizza            |')
    print('|             0 - Retornar ao Menu Principal |')
    print('----------------------------------------------')
    op_pedidos = input("Escolha sua opção: ")
    return op_pedidos

def exibir_cardapio():
    clear_screen()
    print('----------------------------------------------')
    print('|                   Cardápio                 |')
    print('----------------------------------------------')
    cpf = input('Informe seu cpf: ')
    if cpf in clientes:
        clear_screen()
        print('|----------------------------------------------------------------------------------------------------------------------------------|')
        print('|                                                          Cardápio                                                                |')
        print('|----------------------------------------------------------------------------------------------------------------------------------|')
        print('|        |                  |                                                                     |                                |')
        print('|   ID   |       Nome       |                            Ingredientes                             |             Valores            |')
        print('|        |                  |                                                                     |                                |')
        print('|----------------------------------------------------------------------------------------------------------------------------------|')
        for id, pizza in cardapio.items():
            nome = pizza[0]
            ingredientes = ' - '.join(pizza[1])
            valores = ' '.join([f'R$ {float(valor):.2f}' for valor in pizza[2]])
            
            nome_quebrado = textwrap.fill(nome, width=18)
            ingredientes_quebrados = textwrap.fill(ingredientes, width=69)
            valores_quebrados = textwrap.fill(valores, width=10)
            
            linhas_nome = nome_quebrado.split('\n')
            linhas_ing = ingredientes_quebrados.split('\n')
            linhas_valores = valores_quebrados.split('\n')
            
            max_linhas = max(len(linhas_nome), len(linhas_ing), len(linhas_valores))
            for i in range(max_linhas):
                if i == 0:
                    print('|{:^8}'.format(id), end='')
                else:
                    print('|{:^8}'.format(''), end='')
                nome_final = linhas_nome[i] if i < len(linhas_nome) else ''
                ing_final = linhas_ing[i] if i < len(linhas_ing) else ''
                valores_final = linhas_valores[i] if i < len(linhas_valores) else ''
                print('|{:^18}'.format(nome_final), end='')
                print('|{:^69}'.format(ing_final), end='')
                print('|{:^31}'.format(valores_final), '|')
            print('|----------------------------------------------------------------------------------------------------------------------------------|')
    else:
        print('O cpf informado não está cadastrado no nosso sistema')
    print()
    input('Tecle <ENTER> para continuar...')

def cadastrar_pizza():
    clear_screen()
    print('---------------------------------------------------------------')
    print('|                        Cadastrar Pizza                      |')
    print('---------------------------------------------------------------')
    print('|    ID     |      Nome      |    Ingredientes   |    Valor   |')
    print('---------------------------------------------------------------')
    id = f'PI{len(cardapio) + 1}'
    print()
    nome = nome_pizza(cardapio)
    print()
    ingredientes = get_ingredientes()
    print()
    valores = valor_pizza()
    cardapio[id] = [nome, ingredientes, valores]
    print()
    print(f'ID - {id}  |   Nome - {nome}   |   Ingredientes - {ingredientes}   |   Valor P - {valores[0]}   |   Valor M - {valores[1]}  |   Valor G - {valores[2]}  |  Valor GG - {valores[3]}')
    print()
    input('Tecle <ENTER> para continuar...')
    salvar_cardapio()

# def editar_pizza():
#     clear_screen()
#     print('----------------------------------------------')
#     print('|                 Editar Pizza               |')
#     print('----------------------------------------------')
#     id = input('Informe o ID da pizza que deseja fazer a alteração: ')
#     if id in cardapio:
        

def login_fucionarios():
    print('----------------------------------------------')
    print('|                Funcionários                |')
    print('----------------------------------------------')
    print('| Email         | Senha         | Código     |')
    print('----------------------------------------------')

carregar_clientes()
carregar_cardapio()

op_prin = ''
while op_prin != '0':
    op_prin = menu_principal()
    
    if op_prin == '2':
        op_pedidos = ''
        while op_pedidos != '0':
            op_pedidos = menu_pedidos()
            if op_pedidos =='1':
                exibir_cardapio()
            if op_pedidos == '4':
                cadastrar_pizza()



salvar_cardapio()