def carrinho():
    menu_pizzas = {
        "pepperoni": {
            "pequena": 25.00,
            "média": 23.00,
            "grande": 27.00,
            "família": 29.00
        },
        "margherita": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "quatro queijos": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "frango com catupiry": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
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
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "morango com nutella": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "banana com canela": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        },
        "romeu e julieta": {
            "pequena": 28.00,
            "média": 30.00,
            "grande": 32.00,
            "família": 35.00
        }
    }
    verificar = False
    while not verificar:
        opcao = input('Caro cliente, informe o número da pizza desejada (ou 0 para sair): ').lower()
        if opcao == '0':
            print('Obrigado por visitar nossa pizzaria. Volte sempre!')
            break
        if opcao not in menu_pizzas:
            print('Número de pizza inválido. Por favor, informe um número de pizza válido.')
            continue
        pizza_escolhida = menu_pizzas[opcao]
        tamanho = input('Informe o tamanho da sua pizza (pequena/média/grande/família): ').lower()
        if tamanho not in pizza_escolhida:
            print('Tamanho de pizza inválido. Por favor, informe um tamanho válido.')
            continue
        preco_pizza = pizza_escolhida[tamanho]
        print(f"Pedido: {opcao.capitalize()} - Tamanho: {tamanho.capitalize()} - Valor: R${preco_pizza:.2f}")
        adicionar_outra = input("Você deseja adicionar outra pizza ao carrinho? (sim/não): ").lower()
        if adicionar_outra == "não":
            print("Obrigado por fazer seu pedido!")
            break