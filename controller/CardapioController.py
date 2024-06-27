import model.ClientesModel as clm
import model.CardapioModel as cam
import view.CardapioView as cav
import libs.validation as val

clientes = clm.carregar_clientes()
cardapio = cam.carregar_cardapio()

def insert_name(cardapio):
    while True:
        name = cav.get_nome_pizza()
        if val.name_validator(name):
            if any(name == detalhes[0] for detalhes in cardapio.values()):
                print('Essa pizza já está cadastrada no cardápio. Por favor, informe uma nova pizza.')
                continue
            return name

def insert_value():
    while True:
        valores = cav.get_valor()  
        if all(val.isfloat(valor) for valor in valores):
            return [float(valor) for valor in valores]  
        else:
            print('O valor informado é inválido. Por favor, informe somente números.')
            continue

def insert_ingredientes():
    ingredientes = []
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    while True:
        ing = cav.get_ingredientes()
        if val.name_validator(ing):
            ingredientes.append(ing)
            print("Ingredientes até agora:", ' - '.join(ingredientes))
        else:
            print("Ingrediente inválido. Tente novamente.")

        while True:
            resp = input("Deseja adicionar outro ingrediente? (sim/não): ").strip().lower()
            if resp in alternativas:
                break
            print('Resposta inválida. Por favor, escolha entre SIM ou NÃO.')

        if resp in ['n', 'nao', 'não']:
            print('Ingredientes foram adicionados com sucesso.')
            break
    return ingredientes

def cadastrar_pizza():
    cav.cadastrar_pizza()
    id = f'{len(cardapio) + 1}'  
    nome = insert_name(cardapio)
    ingredientes = insert_ingredientes()
    valores = insert_value()
    cardapio[id] = [nome, ingredientes, valores]
    print(f'ID - {id}  |   Nome - {nome}   |   Ingredientes - {ingredientes}   |   Valor P - {valores[0]}   |   Valor M - {valores[1]}  |   Valor G - {valores[2]}  |  Valor GG - {valores[3]}')
    print()
    input('Tecle <ENTER> para continuar...')
    cam.salvar_cardapio(cardapio)

def exibir_cardapio():
    cav.exibir_cardapio()
    cpf = cav.get_cpf()
    if clm.verificar_cpf(cpf):
        dados = cam.formatar_dados(cardapio)
        cav.exibir_dados2(dados)
        fazer_pedido(cpf)
    else:
        print('O CPF informado não está cadastrado no nosso sistema')
    print()
    input('Tecle <ENTER> para continuar...')

def obter_tamanho(tamanhos):
    while True:
        tamanho = cav.get_tamanho()
        if tamanho in tamanhos:
            return tamanho
        else:
            print('O tamanho informado é inválido. Por favor, informe outro.')

def pedido_fazer(alternativas):
    while True:
        request = cav.fazer_pedido()
        if request in alternativas:
            return request
        else:
            print('Resposta inválida. Por favor, escolha entre SIM ou NÃO.')

def solicitar_pizza(cardapio):
    while True:
        id = cav.get_pizza()
        if id not in cardapio:
            print('Pizza não encontrada.')
            continue
        return id

def fazer_pedido(cpf):
    cardapio = cam.carregar_cardapio()
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    tamanhos = ['p', 'm', 'g', 'gg']
    pedidos_existentes = cam.carregar_pedidos()
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
                novo_pedido = cav.get_novo_pedido()
                if novo_pedido in alternativas:
                    break
                print('Resposta inválida. Por favor, escolha entre SIM/NÃO.')
            if novo_pedido in ['n', 'nao', 'não']:
                print('Seu pedido foi recebido, para efetuar o pagamento vá para o carrinho.')
                break
        cam.adicionar_pedido(cpf, pedido_cliente)

def carrinho():
    cav.carrinho()
    cpf = cav.get_cpf()
    pedidos = cam.carregar_pedidos()

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
    pedidos = cam.carregar_pedidos()
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    pedidos_cliente = pedidos.get(cpf, {})

    while True:
        resp = cav.pagamento()
        if resp in alternativas:
            break
        else:
            print('Resposta inválida. Por favor, escolha entre SIM/NÃO.')
    if resp in ['s', 'sim']:
        for pedido_id in pedidos_cliente:
            pedido = pedidos_cliente[pedido_id]
            pedido[5] = True  # Marcar como pago
        cam.salvar_pedidos(pedidos)
    elif resp in ['n', 'nao', 'não']:
        cam.del_pedido(cpf)