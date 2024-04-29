import os

#####################################
#####   Projeto Pizzaria - V2   #####
#####################################

resposta = ''
while resposta != '0':
    os.system('clear')
    print('----------------------------------------------')
    print('|         Sistema de Gestão - Pizzaria       |')
    print('----------------------------------------------')
    print('|             1 - Clientes                   |')
    print('|             2 - Funcionários               |')
    print('|             3 - Administração              |')
    print('|             4 - Sobre a Pizzaria           |')
    print('|             0 - Sair                       |')
    print('----------------------------------------------')
    resposta = input("Escolha sua opção: ")
    
    if resposta == '1':
        print()
        print('----------------------------------------------')
        print('|                  Clientes                  |')
        print('----------------------------------------------')
        print('|             1 - Login                      |')
        print('|             2 - Menu                       |')
        print('|             3 - Pedir                      |')
        print('|             4 - Carrinho                   |')
        print('|             5 - Histórico de Pedidos       |')
        print('|             0 - Retornar ao Menu Principal |')
        print('----------------------------------------------')
        print()
        resp2 = input("Escolha sua opção: ")
        print()
        input("Tecle <ENTER> para continuar...")
    elif resposta == '2':
        print()
        print('----------------------------------------------')
        print('|                Funcionários                |')
        print('----------------------------------------------')
        print('|             1 - Login                      |')
        print('|             2 - Controle de Pedidos        |')
        print('|             3 - Estoque                    |')
        print('|             0 - Retornar ao Menu Principal |')
        print('----------------------------------------------')
        print()
        resp2 = input("Escolha sua opção: ")
        print()
        input("Tecle <ENTER> para continuar...")
    elif resposta == '3':
        print()
        print('----------------------------------------------')
        print('|                 Administração              |')
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
    elif resposta == '4':
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