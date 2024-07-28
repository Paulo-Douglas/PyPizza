import Funcionarios.Cardapio.ProdutosModel as prom
import Funcionarios.Cardapio.ProdutosView as prov
import Administração.AdmModel as admm
import Clientes.ClientesModel as clm
import libs.insertes as ins
import libs.utils as ut
import libs.get as gt

def cadastrar_pizza():
    prov.cadastrar_pizza()
    while True:
        conf = ut.confirmacao('funcionário', 'o cadastro de uma nova pizza')
        match conf:
            case '1':
                funcionarios = admm.funcionarios
                cpf = gt.get_cpf()
                if cpf in funcionarios:
                    cardapio = prom.cardapio
                    id = str(len(cardapio) + 1)
                    nome = ins.insert_name_pizza(cardapio)
                    ingredientes = ins.insert_ingredientes()
                    valores = ins.insert_value()
                    estado = True
                    cardapio[id] = [nome, ingredientes, valores, estado]
                    ingredientes_formatados = '-'.join(ingredientes)
                    prom.salvar_cardapio()
                    print(f'ID - {id}  |   Nome - {nome}   |   Ingredientes - {ingredientes_formatados}   |   Valor P - {valores[0]}   |   Valor M - {valores[1]}  |   Valor G - {valores[2]}  |  Valor GG - {valores[3]}')
                    ut.mostrar_mensagem('Pizza cadastrada com sucesso!')
                    break
                else:
                    ut.mensagem_erro('Esse CPF não é válido ou não está cadastrado como funcionário. Por Favor, informe outro CPF.')
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro funcionário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')
                continue

def editar_pizza():
    prov.alterar_dados()
    while True:
        cardapio = prom.cardapio
        dados = prom.formatar_dados(cardapio)
        prov.alterar_dados2(dados)
        conf = ut.confirmacao('funcionário', 'a edição de uma pizza')
        match conf:
            case '1':
                funcionarios = admm.funcionarios
                cpf = gt.get_cpf()
                if cpf in funcionarios:
                    id = prom.solicitar_pizza(cardapio)
                    if id in cardapio and cardapio[id][3] == True:
                        dados = prom.formatar_dados(cardapio)
                        prov.alterar_dados2(dados)
                        prom.editar_pizza(id, cardapio)
                        prom.salvar_cardapio()
                        break
                    else:
                        ut.mostrar_mensagem('ID da pizza inválido ou pizza inativa. Por favor, informe um ID válido de uma pizza ativa.')
                else:
                    ut.mensagem_erro('Esse CPF não é válido ou não está cadastrado como funcionário. Por Favor, informe outro CPF.')
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro funcionário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')

def excluir_pizza():
    prov.excluir_pizza()
    while True:
        cardapio = prom.cardapio
        funcionarios = admm.funcionarios
        cpf = gt.get_cpf()
        if cpf in funcionarios:
            dados = prom.formatar_dados(cardapio)
            prov.exibir_cardapio(dados)
            prom.del_pizza()
            break
        else:
            ut.mensagem_erro('Esse CPF não é válido ou não está cadastrado como funcionário. Por Favor, informe outro CPF.')