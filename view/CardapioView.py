import model.CardapioModel as cam
import libs.utils as ut

def get_cpf():
    return input('Informe seu CPF: ')

def get_nome_pizza():
    return input('Informe o nome da pizza: ')

def get_ingredientes():
    return input('digite o nome do ingrediente que deseja adicionar: ').title()

def get_ing_novo():
    return input('Deseja adicionar mais ingredientes (SIM/NÃO)? ').lower()

def get_valor():
    return [input(f'Digite o valor da Pizza {tamanho}. Informe somente números : ') for tamanho in ['P', 'M', 'G', 'GG']]

def get_pizza():
    return input('Digite o ID da pizza desejada: ').upper()

def get_tamanho():
    return input('Informe o tamanho da pizza (P, M, G, GG): ').lower()

def fazer_pedido():
    return input('Deseja fazer algum pedido (sim/não)? ').lower()

def get_novo_pedido():
    return input('Deseja fazer outro pedido (sim/não)? ').lower()

def pagamento():
    return input('Deseja realizar o pagamento desse(s) pedido(s) (sim/não)? ').lower()

def menu_pedidos():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|                    Vendas                  |')
    print('----------------------------------------------')
    print('|             1 - Menu                       |')
    print('|             2 - Carrinho                   |')
    print('|             3 - Cadastrar Pizza            |')
    print('|             4 - Editar Pizza               |')
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
    print('|----------------------------------------------------------------------------------------------------------------------------------|')
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
    print('|                                                                 Carrinho                                                            |')
    print('|-------------------------------------------------------------------------------------------------------------------------------------|')
    print('|        |                  |                                                                     |             |                     |')
    print('|   ID   |       Nome       |                            Ingredientes                             |   Tamanho   |        Valor        |')
    print('|        |                  |                                                                     |             |                     |')
    print('|-------------------------------------------------------------------------------------------------------------------------------------|')
    for linha in dados_formatados:
        print(linha)
    print('|-------------------------------------------------------------------------------------------------------------------------------------|')
    print(f'O valor total do pedido é: R${valor_total:.2f}')

def confirmar_pedido():
    while True:
        opcao = input('Deseja confirmar o pedido? (sim/não): ').strip().lower()
        if opcao in ['s', 'sim']:
            return True
        elif opcao in ['n', 'nao', 'não']:
            return False
        print('Opção inválida. Por favor, escolha entre SIM ou NÃO.')