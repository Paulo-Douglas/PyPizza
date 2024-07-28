import Funcionarios.Estoque.EstoqueView as esv
import Funcionarios.Estoque.EstoqueModel as esm
import Administração.AdmModel as admm
import libs.insertes as ins
import libs.utils as ut
import libs.get as gt

def cadastrar_estoque():
    esv.cadastrar_item()
    funcionarios = admm.funcionarios
    while True:
        conf = ut.confirmacao('funcionário', 'o cadastro de um novo produto no estoque')
        match conf:
            case '1':
                cpf = gt.get_cpf()
                if cpf in funcionarios:
                    if funcionarios[cpf][2] == 'Estoquista':
                        estoque = esm.estoque
                        id = str(len(estoque) + 1)
                        nome = ins.insert_name_item(estoque)
                        quantidade = ins.insert_quantidade()
                        valor = ins.insert_valor_produto()
                        valor_total = quantidade * valor
                        estado = True
                        estoque[id] = [nome, quantidade, valor, valor_total, estado]
                        esm.salvar_estoque()
                        print(f'ID - {id}  |   Nome - {nome}   |   Quantidade - {quantidade}    |   Valor Unitário - {valor}   |   Valor Total - {valor_total}')
                        ut.mostrar_mensagem('Pizza cadastrada com sucesso!')
                        break
                    else:
                        ut.mostrar_mensagem('Essa função é restrita. Somente estoquistas podem usá-la.')
                        break
                else:
                    ut.mostrar_mensagem('O CPF informado não está cadastrado no nosso sistema ou não pertence a um funcionário..')
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro funcionário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')
                continue

def exibir_estoque():
    esv.exibir_estoque_1()
    funcionarios = admm.funcionarios
    while True:
        conf = ut.confirmacao('funcionário', 'exibição do estoque')
        match conf:
            case '1':
                cpf = gt.get_cpf()
                if cpf in funcionarios:
                    dados = esm.formatar_dados_estoque()
                    esv.exibir_estoque(dados)
                    ut.mostrar_mensagem(' ')
                    break
                else:
                    ut.mostrar_mensagem('O CPF informado não está cadastrado no nosso sistema ou não pertence a um funcionário.')
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro funcionário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')
                continue

def alterar_estoque():
    esv.alterar_item()
    funcionarios = admm.funcionarios
    estoque = esm.estoque
    while True:
        conf = ut.confirmacao('funcionário', 'a alteração dos dados do estoque')
        match conf:
            case '1':
                cpf = gt.get_cpf()
                if cpf in funcionarios:
                    if funcionarios[cpf][2] == 'Estoquista':
                        dados = esm.formatar_dados_estoque()
                        esv.alterar_dado_item(dados)
                        id = esm.solicitar_id()
                        if id in estoque and estoque[id][4] == True:
                            esm.alterar_dados_estoque(id)
                            esm.salvar_estoque()
                            break
                        else:
                            ut.mensagem_erro('O item vinculado com esse ID está inativa no nosso sistema. Para reativá-la, acesse a seção de cadastro.')
                else:
                    ut.mostrar_mensagem('O CPF informado não está cadastrado em nosso sistema ou não pertence a nenhum de nossos funcionários.')
                    break
            case '0':
                break

def del_estoque():
    esv.excluir_item()
    funcionarios = admm.funcionarios
    estoque = esm.estoque
    while True:
        conf = ut.confirmacao('funcionário', 'deletar um item')
        match conf:
            case '1':
                cpf = gt.get_cpf()
                if cpf in funcionarios:
                    if funcionarios[cpf][2] == 'Estoquista':
                        id = esm.solicitar_id()
                        if estoque[id][4] == True:
                            dados = esm.formatar_dados_estoque()
                            esv.exibir_estoque(dados)
                            esm.del_item()
                            ut.mostrar_mensagem('Operação de exclusão cancelada.')
                            break
                        else:
                            ut.mostrar_mensagem('Esse CPF já foi excluído do nosso sistema.')
                            break
                else:
                    ut.mostrar_mensagem('O CPF informado não está cadastrado em nosso sistema ou não pertence a nenhum de nossos funcionários.')
                    break
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro usuário, a opção informada não é válida. Por favor, digite 1 para continuar com a exclusão ou 0 para sair.')
                continue