import libs.insertes as ins
import libs.files as fil
import textwrap
import pickle

cardapio = {}
def carregar_cardapio():
    global cardapio
    try:
        arq_cardapio = open("cardapio.dat", "rb")
        cardapio = pickle.load(arq_cardapio)
    except (FileNotFoundError, EOFError):
        cardapio = {}

pedidos = {}
def carregar_pedidos():
    global pedidos
    try:
        arq_pedidos = open("cardapio.dat", "rb")
        pedidos = pickle.load(arq_pedidos)
    except (FileNotFoundError, EOFError):
        pedidos = {}

def formatar_dados(cardapio):
    dados_formatados = []
    for id, pizza in cardapio.items():
        nome = pizza[0]
        ingredientes = ' - '.join(pizza[1])
        valores = ' '.join([f'R$ {float(valor):.2f}' for valor in pizza[2]])

        nome_quebrado = textwrap.fill(nome, width=18)
        ingredientes_quebrados = textwrap.fill(ingredientes, width=69)
        valores_quebrados = textwrap.fill(valores, width=31)

        linhas_nome = nome_quebrado.split('\n')
        linhas_ing = ingredientes_quebrados.split('\n')
        linhas_valores = valores_quebrados.split('\n')

        max_linhas = max(len(linhas_nome), len(linhas_ing), len(linhas_valores))
        for i in range(max_linhas):
            linha = '|{:^8}'.format(id if i == 0 else '')
            nome_final = '{:^18}'.format(linhas_nome[i]) if i < len(linhas_nome) else '{:^18}'.format('')
            ing_final = '{:^69}'.format(linhas_ing[i]) if i < len(linhas_ing) else '{:^69}'.format('')
            valores_final = '{:^31}'.format(linhas_valores[i]) if i < len(linhas_valores) else '{:^31}'.format('')
            linha += f'|{nome_final}|{ing_final}|{valores_final} |'
            dados_formatados.append(linha)
        dados_formatados.append('|--------|------------------|---------------------------------------------------------------------|--------------------------------|')  # Linha separadora
    return dados_formatados

def formatar_pedidos_cliente(pedidos_cliente):
    dados_formatados = []
    valor_total = 0.0  # Inicializar o total como float

    for id, pedido in pedidos_cliente.items():
        if pedido[5] == False:
            nome = pedido[1]
            ingredientes = ' - '.join(pedido[2])
            tamanho = pedido[3]
            valor = pedido[4]  # Manter o valor como número
            valor_total += valor  # Somar o valor ao total
            valor_formatado = f'R$ {valor:.2f}'

            nome_quebrado = textwrap.fill(nome, width=18)
            ingredientes_quebrados = textwrap.fill(ingredientes, width=69)
            tamanho_quebrado = textwrap.fill(tamanho, width=13)
            valor_quebrado = textwrap.fill(valor_formatado, width=21)

            linhas_nome = nome_quebrado.split('\n')
            linhas_ing = ingredientes_quebrados.split('\n')
            linhas_tamanho = tamanho_quebrado.split('\n')
            linhas_valor = valor_quebrado.split('\n')

            max_linhas = max(len(linhas_nome), len(linhas_ing), len(linhas_tamanho), len(linhas_valor))
            for i in range(max_linhas):
                linha = '|{:^8}'.format(id if i == 0 else '')
                nome_final = '{:^18}'.format(linhas_nome[i]) if i < len(linhas_nome) else '{:^18}'.format('')
                ing_final = '{:^69}'.format(linhas_ing[i]) if i < len(linhas_ing) else '{:^69}'.format('')
                tamanho_final = '{:^13}'.format(linhas_tamanho[i]) if i < len(linhas_tamanho) else '{:^13}'.format('')
                valor_final = '{:^21}'.format(linhas_valor[i]) if i < len(linhas_valor) else '{:^21}'.format('')
                linha += f'|{nome_final}|{ing_final}|{tamanho_final}|{valor_final}|'
                dados_formatados.append(linha)
            dados_formatados.append('|--------|------------------|---------------------------------------------------------------------|-----------------------------------|')  # Linha separadora
    return dados_formatados, valor_total

def del_pedido(cpf):
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    
    while True:
        resp = input('Caro cliente, realmente deseja excluir seus pedidos (sim/não)? ').lower()
        if resp in alternativas:
            break
        print('Resposta inválida. Responda somente com SIM ou NÃO.')
    
    if resp in ['s', 'sim']:
        if cpf in pedidos:
            try:
                del pedidos[cpf]  # Remover pedidos do cliente pelo CPF
                fil.salvar_pedidos(pedidos)
                print('Exclusão bem-sucedida. Até mais.')
            except KeyError:
                print('CPF não encontrado. Nenhuma exclusão realizada.')
        else:
            print('Nenhum pedido encontrado para o CPF informado.')
    else:
        print('Operação de exclusão cancelada.')

def editar_pizza(cardapio):
    alternativas = ['nome', 'ingredientes', 'valores']
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    verificar = True

    while verificar:
        id = input('Informe o ID da pizza que vc deseja alterar os dados.  - Tecle 0 caso não queira fazer alteração: ')
        if id == '0':
            break
        elif id in cardapio:
            while True:
                decisao = input('Qual dado da pizza você deseja alterar (nome, ingredientes, valores)? ').lower()
                if decisao in alternativas:
                    if decisao == 'nome':
                        nome = ins.insert_name_pizza(cardapio)
                        cardapio[id][0] = nome
                    elif decisao == 'ingredientes':
                        ing = ins.insert_ingredientes()
                        cardapio[id][1] = ing
                    else:
                        valores = ins.insert_value()
                        cardapio[id][2] = valores
                    break
                else:
                    print('Dado informado não existe. Escolha entre: nome, ingredientes e valores.')
            
            while True:
                resp = input('Deseja fazer uma nova alteração nesta pizza (sim/não) ? ').lower()
                if resp in resposta:
                    break
                print('Resposta inválida. Por favor, escolha entre SIM/NÃO.')
            
            if resp in ['n', 'nao', 'não']:
                print('Alterações feitas com sucesso!!')
                verificar = False
        else:
            print('ID da pizza inválido. Por favor, informe um ID válido.')
    fil.salvar_cardapio(cardapio)

carregar_cardapio()
carregar_pedidos()