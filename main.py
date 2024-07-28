# Importações Clientes
import Clientes.ClientesController as clc
import Clientes.ClientesModel as clm
import Clientes.ClientesView as clv

# Importações Vendas
import Vendas.CardapioController as cac
import Vendas.CardapioModel as cam
import Vendas.CardapioView as cav

# Importações Funcionarios
import Funcionarios.FuncionariosController as fuc
import Funcionarios.FuncionariosModel as fum
import Funcionarios.FuncionariosView as fuv

# Importações Produtos
import Funcionarios.Cardapio.ProdutosController as proc
import Funcionarios.Cardapio.ProdutosModel as prom
import Funcionarios.Cardapio.ProdutosView as prov

# Importações Estoque
import Funcionarios.Estoque.EstoqueController as esc
import Funcionarios.Estoque.EstoqueModel as esm
import Funcionarios.Estoque.EstoqueView as esv

# Importações Adm
import Administração.AdmController as admc
import Administração.AdmModel as admm
import Administração.AdmView as admv

# Importações Libs
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
prom.carregar_cardapio()
cam.carregar_pedidos()
esm.carregar_estoque()
admm.carregar_funcionarios()
admm.carregar_adm()

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
            elif op_pedidos == '3':
                cac.cadastrar_pizza()
            elif op_pedidos == '4':
                cac.editar_pizza()
    
    elif op_prin == '3':
        op_func = ''
        while op_func != '0':
            op_func = fuv.menu_funcionario()
            if op_func == '1':
                op_contrl_card = ''
                while op_contrl_card != '0':
                    op_contrl_card = prov.menu_controle_cardapio()
                    if op_contrl_card == '1':
                        proc.cadastrar_pizza()
                    elif op_contrl_card == '2':
                        proc.editar_pizza()
                    elif op_contrl_card == '3':
                        proc.excluir_pizza()
            elif op_func == '2':
                op_estoque = ''
                while op_estoque != '0':
                    op_estoque = esv.menu_estoque()
                    if op_estoque == '1':
                        esc.cadastrar_estoque()
                    elif op_estoque == '2':
                        esc.exibir_estoque()
                    elif op_estoque == '3':
                        esc.alterar_estoque()
                    elif op_estoque == '4':
                        esc.del_estoque()
    
    elif op_prin == '4':
        op_adm = ''
        while op_adm != '0':
            op_adm = admv.menu_adm()
            if op_adm == '3':
                op_ger_fun = ''
                while op_ger_fun != '0':
                    op_ger_fun = admv.gerenciar_funcionarios()
                    if op_ger_fun == '1':
                        admc.cadastrar_funcionario()
                    

clm.salvar_clientes()
prom.salvar_cardapio()
cam.salvar_pedidos()
esm.salvar_estoque()
admm.salvar_funcionarios()
admm.salvar_adm()