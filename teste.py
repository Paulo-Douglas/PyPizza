
def fazer_pedido(cpf):
    cardapio = cam.carregar_cardapio()
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    tamanhos = ['p', 'm', 'g', 'gg']
    pedido_cliente = {}
    
    request = pedido_fazer(alternativas)
    print()
    if request in ['s', 'sim']:
        while True:
            id = cav.get_pizza()
            if id not in cardapio:
                print('Pizza não encontrada.')
                continue
            
            tamanho = obter_tamanho(tamanhos)
            print()
            nome = cardapio[id][0]
            ingredientes = cardapio[id][1]
            valor = cardapio[id][2][tamanhos.index(tamanho)]
            pedido[id] = [nome, ingredientes, valor]
            pedido_cliente[cpf] = pedido
            while True:
                novo_pedido = cav.get_novo_pedido()
                if novo_pedido in alternativas:
                    break
                print('Resposta inválida. Por favor, escolha entre SIM ou NÃO.')
                
            if novo_pedido in ['n', 'nao', 'não']:
                print('Seu pedido foi recebido, para efetuar o pagamento vá para o carrinho.')
                break
        cam.adicionar_pedido(cpf, pedido_cliente)