import Funcionarios.Estoque.EstoqueView as esv
import libs.insertes as ins
import libs.get as gt
import libs.utils as ut
import textwrap
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

def formatar_dados_estoque(): # Função criada pela IA -> GPT
    dados_formatados = []
    linha_separadora = '|--------|----------------------------------|------------------------------------------|--------------------------------------------|---------------|'

    for id, item in estoque.items():
        nome = item[0]
        quantidade = item[1]
        preco_unitario = item[2]
        preco_total = item[3]

        nome_quebrado = textwrap.fill(nome, width=24)
        quantidade_quebrado = textwrap.fill(str(quantidade), width=10)
        preco_unitario_quebrado = textwrap.fill(f'R$ {float(preco_unitario):.2f}', width=10)
        preco_total_quebrado = textwrap.fill(f'R$ {float(preco_total):.2f}', width=14)

        linhas_nome = nome_quebrado.split('\n')
        linhas_quantidade = quantidade_quebrado.split('\n')
        linhas_preco_unitario = preco_unitario_quebrado.split('\n')
        linhas_preco_total = preco_total_quebrado.split('\n')

        max_linhas = max(len(linhas_nome), len(linhas_quantidade), len(linhas_preco_unitario), len(linhas_preco_total))

        for i in range(max_linhas):
            linha = '|{:^8}'.format(id if i == 0 else '')
            nome_final = '{:^34}'.format(linhas_nome[i]) if i < len(linhas_nome) else '{:^34}'.format('')
            quantidade_final = '{:^42}'.format(linhas_quantidade[i]) if i < len(linhas_quantidade) else '{:^42}'.format('')
            preco_unitario_final = '{:^44}'.format(linhas_preco_unitario[i]) if i < len(linhas_preco_unitario) else '{:^44}'.format('')
            preco_total_final = '{:^15}'.format(linhas_preco_total[i]) if i < len(linhas_preco_total) else '{:^15}'.format('')
            linha += f'|{nome_final}|{quantidade_final}|{preco_unitario_final}|{preco_total_final}|'
            dados_formatados.append(linha)

        dados_formatados.append(linha_separadora)  # Linha separadora

    return dados_formatados

def solicitar_id():
    while True:
        id = gt.get_item()
        if id in estoque:
            return id
        else:
            ut.mensagem_erro('Item não encontrada.')
            continue

def alterar_dados_estoque(id):
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    while True:
        decisao = input('Qual dado você deseja alterar? - Tecle 0 caso não queira fazer alteração: ')
        match decisao:
            case '0':
                return False
            case '1':
                nome = ins.insert_name_item()
                estoque[id][0] = nome
                salvar_estoque()
                dados = formatar_dados_estoque()
                esv.exibir_estoque(dados)
                print('Nome alterado com sucesso')
            case '2':
                quantidade = ins.insert_quantidade()
                estoque[id][1] = quantidade
                estoque[id][3] = estoque[id][2] * quantidade
                salvar_estoque()
                dados = formatar_dados_estoque()
                esv.exibir_estoque(dados)
                print('Quantidade alterada com sucesso')
            case '3':
                valor = ins.insert_valor_produto()
                estoque[id][2] = valor
                estoque[id][3] = estoque[id][1] * valor
                salvar_estoque()
                dados = formatar_dados_estoque()
                esv.exibir_estoque()
                print('Valor Unitário alterado com sucessso')
            case _:
                ut.mensagem_erro('Escolha inválida. Escolha entre: 1 para Nome, 2 para Quantidade e 3 para Valor Unitário.')
                continue

        while True:
            resp = input('Deseja fazer uma nova alteração neste item (sim/não)? ').lower().strip()
            if resp not in resposta:
                ut.mensagem_erro('Resposta inválida. Responda com somente SIM ou NÃO.')
                continue
            if resp in ['n', 'nao', 'não']:
                ut.mostrar_mensagem('Alterações feitas com sucesso!!')
                return False
            break

def del_item():
    while True:
        conf = ut.confirmacao('funcionário', 'a exclusão de um item')
        match conf:
            case '1':
                estoque[id][4] = False
                salvar_estoque()
                ut.mostrar_mensagem('Exclusão bem-sucedida. Até mais.')
                break
            case '0':
                ut.mostrar_mensagem('Operação de exclusão cancelada.')
                break
            case _:
                ut.mensagem_erro('Resposta informada não é válida. Escolha entre: 1 (continuar com a exclusão) e 2 (sair).')

carregar_estoque()