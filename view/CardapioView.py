import model.CardapioModel as cam
import libs.utils as ut

def confirmar_pedido():
    while True:
        opcao = input('Deseja confirmar o pedido? (sim/não): ').strip().lower()
        if opcao in ['s', 'sim']:
            return True
        elif opcao in ['n', 'nao', 'não']:
            return False
        print('Opção inválida. Por favor, escolha entre SIM ou NÃO.')

def menu_pedidos():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                    Vendas                  |')
    print('----------------------------------------------')
    print('|             1 - Menu                       |')
    print('|             2 - Carrinho                   |')
    print('|             3 - Cadastrar Pizza            |')
    print('|             4 - Editar Pizza               |')
    print('|             5 - Excluir Pizza              |')
    print('|             0 - Retornar ao Menu Principal |')
    print('----------------------------------------------')
    op_pedidos = input("Escolha sua opção: ")
    return op_pedidos

def cadastrar_pizza():
    ut.clear_screen()
    print('---------------------------------------------------------------')
    print('|                        Cadastrar Pizza                      |')
    print('---------------------------------------------------------------')
    print('|    ID     |      Nome      |    Ingredientes   |    Valor   |')
    print('---------------------------------------------------------------')

def exibir_cardapio():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                   Cardápio                 |')
    print('----------------------------------------------')

def exibir_dados2(dados):
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

def carrinho():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                   Carrinho                 |')
    print('----------------------------------------------')

def carrinho2(pedidos_clientes):
    ut.clear_screen()
    dados_formatados, valor_total = cam.formatar_pedidos_cliente(pedidos_clientes)
    print('|-------------------------------------------------------------------------------------------------------------------------------------|')
    print('|                                                            Carrinho                                                                 |')
    print('|-------------------------------------------------------------------------------------------------------------------------------------|')
    print('|        |                  |                                                                     |             |                     |')
    print('|   ID   |       Nome       |                            Ingredientes                             |   Tamanho   |        Valor        |')
    print('|        |                  |                                                                     |             |                     |')
    print('|-------------------------------------------------------------------------------------------------------------------------------------|')
    for linha in dados_formatados:
        print(linha)
    print('|-------------------------------------------------------------------------------------------------------------------------------------|')
    print(f'O valor total do pedido é: R${valor_total:.2f}')
