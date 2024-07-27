import pickle

estoque = {}

def carregar_estoque(): 
    global estoque
    try:
        arq_estoque = open("estoque.dat", "rb")
        estoque = pickle.load(arq_estoque)
    except (FileNotFoundError, EOFError):
        arq_estoque = open("estoque.dat", "wb")
    arq_estoque.close()

def salvar_estoque():
    arq_estoque = open("estoque.dat", "wb")
    pickle.dump(estoque, arq_estoque)
    arq_estoque.close()

def formatar_dados_estoque(estoque):
    dados_formatados = []
    for id, item in estoque.items():
        nome = item[0]
        quantidade = item[1]
        preco = item[2]

        linha = f"| {id:<8} | {nome:<20} | {quantidade:<10} | {preco:<10.2f} |"
        dados_formatados.append(linha)
        dados_formatados.append("|----------|----------------------|------------|------------|")
    return dados_formatados

carregar_estoque()