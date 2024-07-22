import libs.utils as ut

def menu_funcionario():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                Funcionários                |')
    print('----------------------------------------------')
    print('|            1 - Controle do Cardápio        |')
    print('|            2 - Estoque                     |')
    print('|            0 - Retornar ao Menu Principal  |')
    print('----------------------------------------------')
    op_funcio = input('Escolha sua opção: ')
    return op_funcio

def menu_controle_cardapio():
    ut.clear_screen()
    print('---------------------------------------------------------------')
    print('|                    Controle do Cardápio                     |')
    print('---------------------------------------------------------------')
    print('|                       1 - Cadastrar Pizza                   |')
    print('|                       2 - Editar Pizza                      |')
    print('|                       3 - Excluir Pizza                     |')
    print('|                 0 - Retornar ao Menu Funcioários            |')
    print('---------------------------------------------------------------')
    op_contrl_card = input('Escolha sua opção: ')
    return op_contrl_card

def cadastrar_pizza():
    ut.clear_screen()
    print('---------------------------------------------------------------')
    print('|                        Cadastrar Pizza                      |')
    print('---------------------------------------------------------------')
    print('|    ID     |      Nome      |    Ingredientes   |    Valor   |')
    print('---------------------------------------------------------------')

def alterar_dados():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                Alterar Dados               |')
    print('----------------------------------------------')

def alterar_dados2(dados):
    ut.clear_screen()
    print('|----------------------------------------------------------------------------------------------------------------------------------|')
    print('|                                                     Alterar Dados                                                                |')
    print('|----------------------------------------------------------------------------------------------------------------------------------|')
    print('|    Digite 1 para alterar -> Nome      |    Digite 2 para alterar -> Ingredientes      |   Digite 2 para alterar -> Valores       |')
    print('|----------------------------------------------------------------------------------------------------------------------------------|')
    for linha in dados:
        print(linha)
    print('|----------------------------------------------------------------------------------------------------------------------------------|')

def excluir_pizza():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                Excluir Cliente             |')
    print('----------------------------------------------')

def exibir_cardapio(dados):
    ut.clear_screen()
    print('|----------------------------------------------------------------------------------------------------------------------------------|')
    print('|                                                          Cardápio                                                                |')
    print('|----------------------------------------------------------------------------------------------------------------------------------|')
    print('|        |                  |                                                                     |                                |')
    print('|   ID   |       Nome       |                            Ingredientes                             |             Valores            |')
    print('|        |                  |                                                                     |                                |')
    print('|--------|------------------|---------------------------------------------------------------------|--------------------------------|')
    for linha in dados:
        print(linha)
    print('|----------------------------------------------------------------------------------------------------------------------------------|')
