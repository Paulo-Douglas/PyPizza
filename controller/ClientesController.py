import model.ClientesModel as clm
import view.ClientesView as clv
import libs.insertes as ins
import libs.files as fil
import libs.get as gt

clientes = fil.carregar_clientes()

def register_client():
    clv.cadastrar_clientes()
    nome = ins.insert_name()
    cpf = ins.insert_cpf()
    endereco = ins.insert_address()
    clientes[cpf] = [nome, endereco]
    fil.salvar_clientes(clientes)

def dados_exibir():
    clv.exibir_dados1()
    cpf = gt.get_cpf()
    nome, endereco = clm.chamar_dados(cpf)
    if nome and endereco:
        clv.dados_clientes(cpf, nome, endereco)
    else:
        print("CPF não encontrado no sistema.")
    input('Tecle <ENTER> para continuar...')

def dados_alterar():
    clv.alterar_dados()
    cpf = gt.get_cpf()
    if cpf in clientes:
        nome, endereco = clm.chamar_dados(cpf)
        clv.dados_clientes(cpf, nome, endereco)
        clm.alt_decisao(cpf)
        fil.salvar_clientes(clientes)
    else:
        print('O CPF informado não está cadastrado no nosso sistema.')
    input('Tecle <ENTER> para continuar...')

def cliente_excluir():
    clv.excluir_cliente()
    cpf = gt.get_cpf()
    if cpf in clientes:
        nome, endereco = clm.chamar_dados(cpf)
        clv.dados_clientes(cpf, nome, endereco)
        clm.del_cliente(cpf)
        fil.salvar_clientes(clientes)
    else:
        print('O CPF informado não está cadastrado no nosso sistema.')
    input('Tecle <ENTER> para continuar...')
