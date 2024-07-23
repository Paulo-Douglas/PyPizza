import Funcionarios.FuncionariosModel as fum
import Funcionarios.FuncionariosView as fuv
import Clientes.ClientesModel as clm
import libs.insertes as ins
import libs.utils as ut
import libs.get as gt

def cadastrar_pizza():
    fuv.cadastrar_pizza()
    while True:
        conf = ut.confirmacao('funcionário', 'o cadastro de uma nova pizza')
        match conf:
            case '1':
                cardapio = fum.cardapio
                id = len(cardapio) + 1  
                nome = ins.insert_name_pizza(cardapio)
                ingredientes = ins.insert_ingredientes()
                valores = ins.insert_value()
                estado = True
                cardapio[id] = [nome, ingredientes, valores, estado]
                ingredientes_formatados = '-'.join(ingredientes)
                fum.salvar_cardapio()
                print(f'ID - {id}  |   Nome - {nome}   |   Ingredientes - {ingredientes_formatados}   |   Valor P - {valores[0]}   |   Valor M - {valores[1]}  |   Valor G - {valores[2]}  |  Valor GG - {valores[3]}')
                ut.mostrar_mensagem('Pizza cadastrada com sucesso!')
                break
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro funcionário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')
                continue

def editar_pizza():
    fuv.alterar_dados()
    while True:
        conf = ut.confirmacao('funcionário', 'a edição de uma pizza')
        match conf:
            case '1':
                cardapio = fum.cardapio
                clientes = clm.clientes
                cpf = gt.get_cpf()
                if cpf in clientes:
                    dados = fum.formatar_dados(cardapio)
                    fuv.alterar_dados2(dados)
                    fum.editar_pizza(cardapio)
                    fum.salvar_cardapio()
                    return
                else:
                    ut.mostrar_mensagem('O CPF informado não está cadastrado no nosso sistema.')
            case '0':
                return
            case _:
                ut.mensagem_erro('Caro funcionário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')

def excluir_pizza():
    cardapio = fum.cardapio
    cliestes = clm.clientes
    fuv.excluir_pizza()
    while True:
        cpf = gt.get_cpf()
        if cpf in cliestes:
            dados = fum.formatar_dados(cardapio)
            fuv.exibir_cardapio(dados)
            fum.del_pizza()
            break
        else:
            ut.mensagem_erro('CPF não encontrado. Nenhuma exclusão realizada.')

