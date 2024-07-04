import pickle

def carregar_dados(arquivo):
    try:
        with open(arquivo, 'rb') as arq:
            dados = pickle.load(arq)
    except (FileNotFoundError, EOFError):
        dados = {}  # Retorna um dicionário vazio se o arquivo não existir ou estiver vazio
    return dados

def salvar_dados(arquivo, dic):
    arquivo = open(arquivo, 'wb')
    pickle.dump(dic, arquivo)
    arquivo.close()

def carregar_cardapio():
    return carregar_dados('cardapio.dat')

def carregar_clientes():
    return carregar_dados('clientes.dat')

def salvar_cardapio(cardapio):
    salvar_dados('cardapio.dat', cardapio)

def salvar_clientes(clientes):
    salvar_dados('clientes.dat', clientes)

def carregar_pedidos():
    return carregar_dados('pedidos.dat')

def salvar_pedidos(pedidos):
    salvar_dados('pedidos.dat', pedidos)

def adicionar_pedido(cpf, pedido):  # função criada pelo aluno - Paulo Douglas. Adaptada por: Copilot
    pedidos = carregar_pedidos()
    if cpf in pedidos:
        pedidos[cpf].update(pedido)  # Atualizar pedidos existentes
    else:
        pedidos[cpf] = pedido
    salvar_pedidos(pedidos)

def adicionar_clientes(cpf, nome, endereco):
    global clientes
    clientes[cpf] = [nome, endereco]
    salvar_clientes()