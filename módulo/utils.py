import pickle

menu_pizzas = {
        "pepperoni": {
            "pequena": 25.00,
            "média": 23.00,
            "grande": 27.00,
            "família": 29.00
        },
        "margherita": {
            "pequena": 25.00,
            "média": 23.00,
            "grande": 27.00,
            "família": 29.00
        },
        "quatro queijos": {
            "pequena": 25.00,
            "média": 23.00,
            "grande": 27.00,
            "família": 29.00
        },
        "frango com catupiry": {
            "pequena": 25.00,
            "média": 23.00,
            "grande": 27.00,
            "família": 29.00
        },
        "calabresa": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "portuguesa": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "vegetariana": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "carne seca com rúcula": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "chocolate": {
            "pequena": 20.00,
            "média": 21.00,
            "grande": 22.00,
            "família": 24.00
        },
        "morango com nutella": {
            "pequena": 20.00,
            "média": 21.00,
            "grande": 22.00,
            "família": 24.00
        },
        "banana com canela": {
            "pequena": 20.00,
            "média": 21.00,
            "grande": 22.00,
            "família": 24.00
        },
        "romeu e julieta": {
            "pequena": 20.00,
            "média": 21.00,
            "grande": 22.00,
            "família": 24.00
        }
    }

def validar_opcao(opcao, menu_pizzas):
    if opcao == '0':
        return False
    if opcao not in menu_pizzas:
        print('Nome da pizza inválido. Por favor, informe uma pizza do nosso cardápio.')
        return False
    return True

def validar_tamanho(opcao, tamanho, menu_pizzas):
    pizza_escolhida = menu_pizzas[opcao]
    if tamanho not in pizza_escolhida:
        print('Tamanho de pizza inválido. Por favor, informe um tamanho válido.')
        return False
    return True

def obter_preco(opcao, tamanho, menu_pizzas):
    pizza_escolhida = menu_pizzas[opcao]
    return pizza_escolhida[tamanho]

def adicionar_ao_carrinho(opcao, tamanho, preco_pizza, carrinho):
    pedido = {'opcao': opcao.capitalize(), 'tamanho': tamanho.capitalize(), 'preco': preco_pizza}
    carrinho.append(pedido)
    print(f"Pedido: {pedido['opcao']} - Tamanho: {pedido['tamanho']} - Valor: R${pedido['preco']:.2f}")

def imprimir_recibo(carrinho):
    print("Pedidos realizados:")
    for pedido in carrinho:
        print(f"Pedido: {pedido['opcao']} - Tamanho: {pedido['tamanho']} - Valor: R${pedido['preco']:.2f}")
    print("Obrigado por fazer seu pedido!")

def fazer_pedido():
    carrinho = []
    verificar = True
    while verificar:
        opcao = input('Caro cliente, informe o nome da pizza desejada (ou 0 para sair): ').lower()
        if opcao == '0':
            break
        if not validar_opcao(opcao, menu_pizzas):
            continue
        
        tamanho = input('Informe o tamanho da sua pizza (pequena/média/grande/família): ').lower()
        if not validar_tamanho(opcao, tamanho, menu_pizzas):
            continue
        
        preco_pizza = obter_preco(opcao, tamanho, menu_pizzas)
        adicionar_ao_carrinho(opcao, tamanho, preco_pizza, carrinho)
        
        adicionar_outra = input("Você deseja adicionar outra pizza ao carrinho? (sim/não): ").lower()
        if adicionar_outra != 'sim':
            verificar = False

def validar_numero(fone):
    telefone = ''.join(filter(str.isdigit, fone))  # Remover todos os caracteres que não são dígitos
    if len(telefone) == 10 or len(telefone) == 11 or len(telefone) == 12:
        return True
    else:
        return False

def validar_email(email):
        if '@' in email and '.' in email.split('@')[1]:
            return email
        else:
            return False