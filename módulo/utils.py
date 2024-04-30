def carrinho():
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
    verificar = True
    while verificar:
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
        if adicionar_outra != 'sim':
            print("Obrigado por fazer seu pedido!")
            verificar = False

def validar_email(email):
        if '@' in email and '.' in email.split('@')[1]:
            return email
        else:
            return False

def validar_numero(fone):
    numero_limpo = ''.join(filter(str.isdigit, fone))  # Remover todos os caracteres que não são dígitos
    if len(numero_limpo) == 10:  # Verificar se o número tem 10 dígitos (formato padrão no Brasil)
        return True
    elif len(numero_limpo) == 11 and (numero_limpo[0] == '0' or numero_limpo[0] == '1'): # Verificar se o número tem 11 dígitos (incluindo o DDD)
        return True
    elif len(numero_limpo) == 12 and (numero_limpo[0] == '0' and numero_limpo[1] == '1'): # Verificar se o número tem 12 dígitos (incluindo o DDD com o formato (DDD) 123456789)
        return True
    else:
        print('O número informado é inválido. Por favor, informe um número válido')
        return False