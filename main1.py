import controller.ClientesController as clc
import controller.CardapioController as cac
import view.ClientesView as clv
import view.CardapioView as cav
import model.ClientesModel as clm
import libs.utils as ut

def menu_principal():
    ut.clear_screen()
    print('----------------------------------------------')
    print('|         Sistema de Gestão - Pizzaria       |')
    print('----------------------------------------------')
    print('|             1 - Clientes                   |')
    print('|             2 - Vendas                     |')
    print('|             3 - Funcionários               |')
    print('|             4 - Administração              |')
    print('|             5 - Sobre a Pizzaria           |')
    print('|             0 - Sair                       |')
    print('----------------------------------------------')
    op_prin = input("Escolha sua opção: ")
    return op_prin

clm.carregar_clientes()

op_prin = ''
while op_prin != '0':
    op_prin = menu_principal()
    
    if op_prin == '1':
        op_cliente = ''
        while op_cliente != '0':
            op_cliente = clv.menu_clientes()
            if op_cliente == '1':
                clc.register_client()
            elif op_cliente == '2':
                clc.dados_exibir()
            elif op_cliente == '3':
                clc.dados_alterar()
            elif op_cliente == '4':
                clc.cliente_excluir()
    
    elif op_prin == '2':
        op_pedidos = ''
        while op_pedidos != '0':
            op_pedidos = cav.menu_pedidos()
            if op_pedidos == '1':
                cac.exibir_cardapio()
            elif op_pedidos == '2':
                cac.carrinho()
            elif op_pedidos == '4':
                cac.cadastrar_pizza()

clm.salvar_clientes()