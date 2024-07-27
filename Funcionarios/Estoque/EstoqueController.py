import Funcionarios.Estoque.EstoqueView as esv
import Funcionarios.Estoque.EstoqueModel as esm
import libs.insertes as ins
import libs.utils as ut

def cadastrar_pizza():
    esv.cadastrar_item()
    while True:
        conf = ut.confirmacao('funcionário', 'o cadastro de um novo produto no estoque')
        match conf:
            case '1':
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
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro funcionário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')
                continue