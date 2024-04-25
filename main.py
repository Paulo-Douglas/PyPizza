import os

#####################################
#####   Projeto Pizzaria - V1   #####
#####################################

resposta = ''
while resposta != '0':
    os.system('clear')
    print('----------------------------------------------')
    print('|         Sistema de Gestão - Pizzaria       |')
    print('----------------------------------------------')
    print('|             1 - Módulo Clientes            |')
    print('|             5 - Sobre a Pizzaria           |')
    print('|             0 - Sair                       |')
    print('----------------------------------------------')
    resposta = input("Escolha sua opção: ")
    if resposta == '1':
        print()
        print('----------------------------------------------')
        print('|               Módulo Clientes              |')
        print('----------------------------------------------')
        print('| 1. Menu                                    |')
        print('| 2. Pedir                                   |')
        print('| 3. Promoções                               |')
        print('----------------------------------------------')
        resp = int(input('Escolha uma opção: '))
        if resp == 1:
            print()
        print('----------------------------------------------')
        print('|               Módulo Clientes              |')
        print('----------------------------------------------')
        print('| 1. Menu                                    |')
        print('| 2. Pedir                                   |')
        print('| 3. Promoções                               |')
        print('----------------------------------------------')
    elif resposta == '4':
        print()
        print('----------------------------------------------')
        print('|               Promoções                    |')
        print('----------------------------------------------')
        print('| Promoção da Semana: Na compra de duas      |')
        print('| pizzas, ganhe uma Coca-Cola                |')
        print('----------------------------------------------')
        input("Tecle <ENTER> para continuar...")
    elif resposta == '5':
        print()
        print('----------------------------------------------')
        print('|            Sobre a Pizzaria                |')
        print('----------------------------------------------')
        print('| Projeto de Gestão de Pizzaria.             |')
        print('| Desenvolvidor por: Paulo Douglas.          |')
        print('| Email: paulo.martins.132@ufrn.edu.com      |')
        print('----------------------------------------------')
        input("Tecle <ENTER> para continuar...")