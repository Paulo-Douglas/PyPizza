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