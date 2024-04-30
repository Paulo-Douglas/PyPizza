import os

clientes = {}
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

################################################################
################################################################
##########               F U N Ç Õ E S                ##########
################################################################
################################################################

def validar_email(email):
    if '@' in email and '.' in email.split('@')[1]:
        return email
    else:
        print('O email informado não é válido. Informe outro')

def carrinho():
    verificar = True
    while verificar:
        opcao = input('Caro cliente, informe o nome da pizza desejada (ou 0 para sair): ').lower()
        if opcao == '0':
            print('Obrigado por visitar nossa pizzaria. Volte sempre!')
            break
        if opcao not in menu_pizzas:
            print('Essa pizza não se encontra no nosso menu. Por favor, informe uma pizza válida.')
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

op_prin = ''
while op_prin != '0':
    os.system('clear')
    print('----------------------------------------------')
    print('|         Sistema de Gestão - Pizzaria       |')
    print('----------------------------------------------')
    print('|             1 - Clientes                   |')
    print('|             2 - Menu                       |')
    print('|             3 - Funcionários               |')
    print('|             4 - Administração              |')
    print('|             5 - Sobre a Pizzaria           |')
    print('|             0 - Sair                       |')
    print('----------------------------------------------')
    op_prin = input("Escolha sua opção: ")
    
    if op_prin == '1':
        op_cliente = ''
        while op_cliente !='0':
            os.system('clear')
            print()
            print('----------------------------------------------')
            print('|                   Clientes                 |')
            print('----------------------------------------------')
            print('|             1 - Cadastre - se              |')
            print('|             2 - Exibir Dados               |')
            print('|             3 - Alterar Dados              |')
            print('|             4 - Excluir Cliente            |')
            print('|             0 - Retornar ao Menu Principal |')
            print('----------------------------------------------')
            print()
            op_cliente = input("Escolha sua opção: ")
            print()
            if op_cliente == '1':
                os.system('clear')
                print()
                print('----------------------------------------------')
                print('|                 Cadastre - se              |')
                print('----------------------------------------------')
                print('| Nome   | Telefone   | Email   | Endereço   |')
                print('----------------------------------------------')
                print()
                nome = input('Nome: ')
                print()
                fone = input('Telefone: ')
                print()
                email = input('Email: ')
                while not validar_email(email):
                    print("Por favor, insira um email válido.")
                    email = input('Email: ')
                print()
                endereco = input('Endereço: ')
                print()
                clientes[nome] = [fone, email, endereco]
                print()
                print(clientes)
                print('Cadatro feito com sucesso!!')
                input('Tecle <ENTER> para combinar...')
            elif op_cliente == '2':
                os.system('clear')
                print()
                print('----------------------------------------------')
                print('|                 Exibir Dados               |')
                print('----------------------------------------------')
                print('| Nome   | Telefone   | Email   | Endereço   |')
                print('----------------------------------------------')
                print()
                print('Nome: ', nome)
                print('Telefone: ', fone)
                print('Email: ', email)
                print('Endereço: ', endereco)
                print()
                input('Tecle <ENTER> para combinar...')
            elif op_cliente == '3':
                os.system('clear')
                print()
                print('----------------------------------------------')
                print('|                 Alterar Dados              |')
                print('----------------------------------------------')
                print('| Nome   | Telefone   | Email   | Endereço   |')
                print('----------------------------------------------')
                print()
                nome = input('Nome: ')
                print()
                fone = input('Telefone: ')
                print()
                email = input('Email: ')
                print()
                endereco = input('Endereço: ')
                print()
                print('Dados alterados com sucesso!!')
                input('Tecle <ENTER> para combinar...')
            elif op_cliente == '4':
                os.system('clear')
                print('----------------------------------------------')
                print('|                Excluir Cliente             |')
                print('----------------------------------------------')
                email = input('Email: ')
                print()
                print('Cliente excluido com sucesso!!')
                input('Tecle <ENTER> para combinar...')
    elif op_prin =='2':
        print()
        print('-------------------------------------------------')
        print('|                     Menu                      |')
        print('-------------------------------------------------')
        print('|                Pizzas Salgadas                |')
        print('|-----------------------------------------------|')
        print('| 1. Pepperoni           | R$ 25,00 - Pequena   |')
        print('| 2. Margherita          | R$ 23,00 - média     |')
        print('| 3. Quatro Queijos      | R$ 27,00 - Grande    |')
        print('| 4. Frango com Catupiry | R$ 29,00 - Família   |')
        print('|-----------------------------------------------|')
        print('|                Pizzas Especiais               |')
        print('|-----------------------------------------------|')
        print('| 5. Calabresa             | R$ 28,00 - Pequena |')
        print('| 6. Portuguesa            | R$ 30,00 - Média   |')
        print('| 7. Vegetariana           | R$ 32,00 - Grande  |')
        print('| 8. Carne Seca com Rúcula | R$ 35,00 - Família |')
        print('|-----------------------------------------------|')
        print('|                  Pizzas Doces                 |')
        print('|-----------------------------------------------|')
        print('| 9. Chocolate           | R$ 20,00 - Pequena   |')
        print('|10. Morango com Nutella | R$ 21,00 - Média     |')
        print('|11. Banana com Canela   | R$ 22,00 - Grande    |')
        print('|12. Romeu e Julieta     | R$ 24,00 - Família   |')
        print('|-----------------------------------------------|')
        print('|              Tamanhos Disponíveis             |')
        print('|-----------------------------------------------|')
        print('| Pequena - 6 fatias  | Média - 8 fatias        |')
        print('| Grande - 10 fatias  | Família - 12 fatias     |')
        print('|-----------------------------------------------|')
        print('|          0 - Retornar ao Menu Principal       |')
        print('-------------------------------------------------')
        pedido = carrinho()
    elif op_prin == '4':
        op_func = ''
        while op_func != '0':
            os.system('clear')
            print('----------------------------------------------')
            print('|                Funcionários                |')
            print('----------------------------------------------')
            print('|             1 - Login                      |')
            print('|             2 - Controle de Pedidos        |')
            print('|             3 - Estoque                    |')
            print('|             0 - Retornar ao Menu Principal |')
            print('----------------------------------------------')
            print()
            op_func = input('Escolha uma das opções: ')
            print()
            if op_func == '1':  # só quem pode cadatrar novos funcionários são os adms
                os.system('clear')
                print('----------------------------------------------')
                print('|                Funcionários                |')
                print('----------------------------------------------')
                print('| Email         | Senha         | Código     |')
                print('----------------------------------------------')
                email = input('Informe seu email: ')
                senha = input('Informe sua senha: ')
                codigo = input('Informe seu código de acesso: ')
            if op_func == '2':
                os.system('clear')
    elif op_prin == '5':
        print()
        print('----------------------------------------------')
        print('|                Administração               |')
        print('----------------------------------------------')
        print('|             1 - Relatório de Vendas        |')
        print('|             2 - Despesas                   |')
        print('|             3 - Gestão Geral               |')
        print('|             0 - Retornar ao Menu Principal |')
        print('----------------------------------------------')
        print()
        resp2 = input("Escolha sua opção: ")
        print()
        input("Tecle <ENTER> para continuar...")
    elif op_prin == '6':
        print()
        print('----------------------------------------------')
        print('|            Sobre a Pizzaria                |')
        print('----------------------------------------------')
        print('| Projeto de Gestão de Pizzaria.             |')
        print('| Desenvolvido por: Paulo Douglas.           |')
        print('| Email: paulo.martins.132@ufrn.edu.com      |')
        print('| GitHub: Paulo-Douglas                      |')
        print('----------------------------------------------')
        input("Tecle <ENTER> para continuar...")

print("Você encerrou o programa!")
print("Até logo!")