import Vendas.CardapioModel as cam
import Vendas.CardapioView as cav
import libs.verify as verf
import libs.insertes as ins
import libs.files as fil
import libs.get as gt

clientes = fil.carregar_clientes()
cardapio = fil.carregar_cardapio()

def cadastrar_pizza():
    cav.cadastrar_pizza()
    id = f'{len(cardapio) + 1}'  
    nome = ins.insert_name_pizza(cardapio)
    ingredientes = ins.insert_ingredientes()
    valores = ins.insert_value()
    cardapio[id] = [nome, ingredientes, valores]
    print(f'ID - {id}  |   Nome - {nome}   |   Ingredientes - {ingredientes}   |   Valor P - {valores[0]}   |   Valor M - {valores[1]}  |   Valor G - {valores[2]}  |  Valor GG - {valores[3]}')
    print()
    input('Tecle <ENTER> para continuar...')
    fil.salvar_cardapio(cardapio)

def exibir_cardapio():
    cav.exibir_cardapio()
    cpf = gt.get_cpf()
    if verf.verificar_cpf(cpf):
        dados = cam.formatar_dados(cardapio)
        cav.exibir_dados2(dados)
        fazer_pedido(cpf)
    else:
        print('O CPF informado não está cadastrado no nosso sistema')
    print()
    input('Tecle <ENTER> para continuar...')

def obter_tamanho(tamanhos):
    while True:
        tamanho = gt.get_tamanho()
        if tamanho in tamanhos:
            return tamanho
        else:
            print('O tamanho informado é inválido. Por favor, informe outro.')

def pedido_fazer(alternativas):
    while True:
        request = gt.fazer_pedido()
        if request in alternativas:
            return request
        else:
            print('Resposta inválida. Por favor, escolha entre SIM ou NÃO.')

def solicitar_pizza(cardapio):
    while True:
        id = gt.get_pizza()
        if id not in cardapio:
            print('Pizza não encontrada.')
            continue
        return id

def fazer_pedido(cpf):
    cardapio = fil.carregar_cardapio()
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    tamanhos = ['p', 'm', 'g', 'gg']
    pedidos_existentes = fil.carregar_pedidos()
    pedido_cliente = pedidos_existentes.get(cpf, {})  # Obter pedidos existentes para o CPF
    
    request = pedido_fazer(alternativas)
    if request in ['s', 'sim']:
        while True:
            id = solicitar_pizza(cardapio)
            tamanho = obter_tamanho(tamanhos)
            nome = cardapio[id][0]
            ingredientes = cardapio[id][1]
            pagamento = False
            valor = cardapio[id][2][tamanhos.index(tamanho)]
            
            pedido_cliente[len(pedido_cliente) + 1] = [id, nome, ingredientes, tamanho, valor, pagamento]
            
            while True:
                novo_pedido = gt.get_novo_pedido()
                if novo_pedido in alternativas:
                    break
                print('Resposta inválida. Por favor, escolha entre SIM/NÃO.')
            if novo_pedido in ['n', 'nao', 'não']:
                print('Seu pedido foi recebido, para efetuar o pagamento vá para o carrinho.')
                break
        fil.adicionar_pedido(cpf, pedido_cliente)

def carrinho():
    cav.carrinho()
    cpf = gt.get_cpf()
    pedidos = fil.carregar_pedidos()

    if cpf in pedidos:
        pedidos_cliente = {k: v for k, v in pedidos[cpf].items() if not v[5]}  # Filtrar apenas os pedidos não pagos
        if pedidos_cliente:
            cav.carrinho2(pedidos_cliente)
            pagamentos(cpf)
        else:
            print('Nenhum pedido não pago encontrado para o CPF informado.')
    else:
        print('Nenhum pedido encontrado para o CPF informado.')
    
    print()
    input('Tecle <ENTER> para continuar...')

def pagamentos(cpf):
    pedidos = fil.carregar_pedidos()
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    pedidos_cliente = pedidos.get(cpf, {})

    while True:
        resp = gt.pagamento()
        if resp in alternativas:
            break
        else:
            print('Resposta inválida. Por favor, escolha entre SIM/NÃO.')
    if resp in ['s', 'sim']:
        for pedido_id in pedidos_cliente:
            pedido = pedidos_cliente[pedido_id]
            pedido[5] = True  # Marcar como pago
        fil.salvar_pedidos(pedidos)
    elif resp in ['n', 'nao', 'não']:
        cam.del_pedido(cpf)

def editar_pizza():
    cav.exibir_cardapio()
    cpf = gt.get_cpf()
    if cpf in clientes:
        dados = cam.formatar_dados(cardapio)
        cav.exibir_dados2(dados)
        cam.editar_pizza(cardapio)
        fil.salvar_cardapio(cardapio)
    else:
        print('O CPF informado não está cadastrado no nosso sistema.')
    input('Tecle <ENTER> para continuar...')

