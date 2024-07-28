import Funcionarios.Cardapio.ProdutosView as prov
import Clientes.ClientesModel as clm
import libs.insertes as ins
import libs.utils as ut
import libs.get as gt
import textwrap
import pickle

cardapio = {}

def carregar_cardapio(): # Função adaptada pela IA -> GPT
    global cardapio
    try:
        arq_cardapio = open("cardapio.dat", "rb")
        cardapio = pickle.load(arq_cardapio)
    except (FileNotFoundError, EOFError):
        arq_cardapio = open("cardapio.dat", "wb")
    arq_cardapio.close()

def salvar_cardapio():
    arq_cardapio = open("cardapio.dat", "wb")
    pickle.dump(cardapio, arq_cardapio)
    arq_cardapio.close()

def formatar_dados(cardapio): # Função criada pela IA -> GPT
        dados_formatados = []
        for id, pizza in cardapio.items():
            if pizza[3] == False:
                continue  # Ignora pizzas com estado False

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
                nome_final = '{:^38}'.format(linhas_nome[i]) if i < len(linhas_nome) else '{:^38}'.format('')
                ing_final = '{:^47}'.format(linhas_ing[i]) if i < len(linhas_ing) else '{:^47}'.format('')
                valores_final = '{:^41}'.format(linhas_valores[i]) if i < len(linhas_valores) else '{:^41}'.format('')
                linha += f'|{nome_final}|{ing_final}|{valores_final} |'
                dados_formatados.append(linha)
            dados_formatados.append('|--------|--------------------------------------|-----------------------------------------------|------------------------------------------|')  # Linha separadora
        return dados_formatados

def solicitar_pizza(cardapio):
    while True:
        id = gt.get_pizza()
        if id in cardapio:
            return id
        else:
            ut.mensagem_erro('Pizza não encontrada.')
            continue

def editar_pizza(id, cardapio):
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    while True:
        decisao = input('Qual dado da pizza você deseja alterar? ')
        match decisao:
            case '1':
                nome = ins.insert_name_pizza(cardapio)
                cardapio[id][0] = nome
                dados = formatar_dados(cardapio)
                prov.alterar_dados2(dados)
                print('Nome da pizza alterado com sucesso.')
            case '2':
                ingredientes = ins.insert_ingredientes()
                cardapio[id][1] = ingredientes
                dados = formatar_dados(cardapio)
                prov.alterar_dados2(dados)
                print('Ingredientes da pizza alterados com sucesso.')
            case '3':
                valores = ins.insert_value()
                cardapio[id][2] = valores
                dados = formatar_dados(cardapio)
                prov.alterar_dados2(dados)
                print('Valores da pizza alterados com sucesso.')
            case _:
                ut.mensagem_erro('Escolha inválida. Escolha entre: 1 para Nome, 2 para Ingredientes e 3 para Valores.')
                continue

        while True:
            resp = input('Deseja fazer uma nova alteração nesta pizza (sim/não)? ').lower().strip()
            if resp not in resposta:
                ut.mensagem_erro('Resposta inválida. Responda com somente SIM ou NÃO.')
                continue
            if resp in ['n', 'nao', 'não']:
                ut.mostrar_mensagem('Alterações feitas com sucesso!!')
                return False
            break

def del_pizza():
    while True:
        conf = ut.confirmacao('funcionário', 'a exclusão de uma pizza')
        match conf:
            case '1':
                id = solicitar_pizza(cardapio)
                cardapio[id][3] = False
                salvar_cardapio()
                ut.mostrar_mensagem('Exclusão bem-sucedida. Até mais.')
                break
            case '0':
                ut.mostrar_mensagem('Operação de exclusão cancelada.')
                break
            case _:
                ut.mensagem_erro('Resposta informada não é válida. Escolha entre: 1 (continuar com a exclusão) e 2 (sair).')

carregar_cardapio()