import Clientes.ClientesModel as clm
import Clientes.ClientesView as clv
import libs.insertes as ins
import libs.get as gt
import libs.utils as ut

def register_client():
    clientes = clm.clientes
    clv.cadastrar_clientes()
    while True:
        conf = ut.confirmacao('cliente','um cadastro')
        match conf:
            case '1':
                nome = ins.insert_name()
                cpf = ins.insert_cpf()
                endereco = ins.insert_address()
                clientes = clm.clientes
                clientes[cpf] = [nome, endereco]
                print(f'Nome - {nome} | CPF - {cpf} | Endereço - {endereco}')
                print()
                ut.mostrar_mensagem('Cliente cadastrado com sucesso!')
                break
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro usuário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')

def dados_exibir():
    clv.exibir_dados1()
    while True:
        conf = ut.confirmacao('cliente', 'a exibição dos seu dados')
        match conf:
            case '1':
                cpf = gt.get_cpf()
                clientes = clm.clientes
                if cpf in clientes:
                    nome, endereco = clm.chamar_dados(cpf, clientes)
                    clv.dados_clientes(cpf, nome, endereco)
                else:
                    ut.mostrar_mensagem('O CPF informado não está cadastrado no nosso sistema.')
                    break
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro usuário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')
                continue

def dados_alterar():
    clv.alterar_dados()
    while True:
        conf = ut.confirmacao('cliente', 'a alteração dos seus dados')
        match conf:
            case '1':
                cpf = gt.get_cpf()
                clientes = clm.clientes
                if cpf in clientes:
                    nome, endereco = clm.chamar_dados(cpf, clientes)
                    clv.alterar_dados2(cpf, nome, endereco)
                    if not clm.alt_decisao(cpf, clientes):
                        break
                    else:
                        clm.salvar_clientes()
                else:
                    ut.mensagem_erro('O CPF informado não está cadastrado no nosso sistema.')
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro usuário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')

def cliente_excluir():
    clv.excluir_cliente()
    while True:
        conf = ut.confirmacao('cliente', 'deletar sua conta')
        match conf:
            case '1':
                cpf = gt.get_cpf()
                clientes = clm.clientes
                if cpf in clientes:
                    nome, endereco = clm.chamar_dados(cpf, clientes)
                    clv.dados_clientes(cpf, nome, endereco)
                    clm.del_cliente(cpf, clientes)
                else:
                    ut.mostrar_mensagem('O CPF informado não está cadastrado no nosso sistema.')
                    break
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro usuário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')
                continue