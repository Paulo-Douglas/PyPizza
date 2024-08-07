import libs.utils as ut

def relatorio_clientes():
    ut.clear_screen()
    print('------------------------------------------------')
    print('|              Relatórios de Clientes          |')
    print('------------------------------------------------')
    print('|          1 - Clientes Ativos                 |')
    print('|          2 - Clientes Inativos               |')
    print('|          0 - Retornar ao Menu Principal      |')
    print('------------------------------------------------')
    op_rel_clien = input('Escolha sua opção: ')
    return op_rel_clien

def exibir_dados_clien_ativos():
    ut.clear_screen()
    print('----------------------------------------------------------------')
    print('|                 Exibir Dados Clientes Ativos                 |')
    print('----------------------------------------------------------------')

def exibir_dados_clien_inativos():
    ut.clear_screen()
    print('----------------------------------------------------------------')
    print('|                 Exibir Dados Clientes Inativos               |')
    print('----------------------------------------------------------------')

def dados_clientes_ativos(dados_formatados):
    ut.clear_screen()
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    print('|                                                     Dados Cliente Ativos                                                        |')
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    print('|                    Nome                     |       CPF       |                            Endereço                             |')
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    for linha in dados_formatados:
        print(linha)
    print('|---------------------------------------------------------------------------------------------------------------------------------|')

def dados_clientes_inativos(dados_formatados):
    ut.clear_screen()
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    print('|                                                    Dados Cliente Inativos                                                       |')
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    print('|                    Nome                     |       CPF       |                            Endereço                             |')
    print('|---------------------------------------------------------------------------------------------------------------------------------|')
    for linha in dados_formatados:
        print(linha)
    print('|---------------------------------------------------------------------------------------------------------------------------------|')