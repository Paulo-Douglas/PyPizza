import libs.utils as ut

def menu_clientes():
    ut.clear_screen()
    print()
    print('----------------------------------------------')
    print('|                  Clientes                  |')
    print('----------------------------------------------')
    print('|             1 - Cadastre - se              |')
    print('|             2 - Exibir Dados               |')
    print('|             3 - Alterar Dados              |')
    print('|             4 - Excluir Cliente            |')
    print('|             0 - Retornar ao Menu Principal |')
    print('----------------------------------------------')
    op_cliente = input("Escolha sua opção: ")
    return op_cliente

def confirmacao(texto):
    return input(f'Você quer mesmo realizar {texto}? -> Digite 1 para continuar e 0 para sair ').strip()

def cadastrar_clientes():
    ut.clear_screen()
    print()
    print('----------------------------------------------')
    print('|                Cadastre - se               |')
    print('----------------------------------------------')
    print('|      Nome      |    CPF    |    Endereço   |')
    print('----------------------------------------------')

def exibir_dados1():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                 Exibir Dados               |')
    print('----------------------------------------------')

def alterar_dados():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                Alterar Dados               |')
    print('----------------------------------------------')

def excluir_cliente():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                Excluir Cliente             |')
    print('----------------------------------------------')

def dados_clientes(cpf, nome, endereco):
    ut.clear_screen()
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    print('|                                                     Dados Cliente                                                               |')
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    print('|                    Nome                     |       CPF       |                            Endereço                             |')
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    print('|{:^45}'.format(nome), end='')
    print('|{:^17}'.format(cpf), end='')
    print('|{:^64}'.format(endereco), '|')
    print('|---------------------------------------------------------------------------------------------------------------------------------|')

def alterar_dados():
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    print('|                                                     Alterar Dados                                                               |')
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    print('|    Digite 1 para alterar -> Nome      |    Digite 2 para alterar -> CPF      |   Digite 2 para alterar -> Endereço              |')
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
