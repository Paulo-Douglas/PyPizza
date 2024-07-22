import Funcionarios.FuncionariosModel as fum
import Vendas.CardapioModel as cam
import Vendas.CardapioView as cav
import libs.verify as verf
import libs.insertes as ins
import libs.get as gt
import libs.utils as ut

def exibir_cardapio():
    cav.exibir_cardapio()
    while True:
        conf = ut.confirmacao('cliente', 'a exibição do cardápio')
        match conf:
            case '1':
                cardapio = fum.cardapio
                cpf = gt.get_cpf()
                if verf.verificar_cpf(cpf):
                    dados = fum.formatar_dados(cardapio)
                    cav.exibir_dados2(dados)
                    fazer_pedido(cpf)
                else:
                    ut.mensagem_erro('O CPF informado não está cadastrado no nosso sistema')
                break
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro usuário, a opção informada não é válida. Por favor, digite 1 para continuar com o cadastro e 0 para sair.')
                continue

def obter_tamanho(tamanhos):
    while True:
        tamanho = gt.get_tamanho()
        if tamanho in tamanhos:
            return tamanho
        else:
            ut.mensagem_erro('O tamanho informado é inválido. Por favor, informe outro.')

def pedido_fazer():
    while True:
        request = gt.fazer_pedido()
        match request:
            case '1':
                return request
            case '0':
                return
            case _:
                ut.mensagem_erro('Resposta inválida. Por favor, escolha entre 1 para SIM ou 0 para NÃO.')
                continue

def solicitar_pizza(cardapio):
    while True:
        id = gt.get_pizza()
        id = int(id)
        if id in cardapio:
            return id
        else:
            ut.mensagem_erro('Pizza não encontrada.')
            continue

def fazer_pedido(cpf):
    cardapio = fum.cardapio

    tamanhos = ['p', 'm', 'g', 'gg']
    pedidos_existentes = cam.pedidos
    pedido_cliente = pedidos_existentes.get(cpf, {})  # Obter pedidos existentes para o CPF
    
    request = pedido_fazer()
    if request:
        while True:
            id = solicitar_pizza(cardapio)
            tamanho = obter_tamanho(tamanhos)
            nome = cardapio[id][0]
            ingredientes = cardapio[id][1]
            pagamento = False
            valor = cardapio[id][2][tamanhos.index(tamanho)]

            # Gere um novo ID para o pedido
            novo_id_pedido = len(pedido_cliente) + 1
            
            # Adicione o novo pedido ao dicionário
            pedido_cliente[novo_id_pedido] = [id, nome, ingredientes, tamanho, valor, pagamento]
            
            while True:
                novo_pedido = gt.get_novo_pedido()
                match novo_pedido:
                    case '1':
                        break  # Voltar ao loop externo para fazer um novo pedido
                    case '0':
                        ut.mensagem_erro('Seu pedido foi recebido, para efetuar o pagamento vá para o carrinho.')
                        cam.pedidos[cpf] = pedido_cliente  # Salvar o pedido do cliente
                        cam.salvar_pedidos()
                        return  # Sair da função após finalizar o pedido
                    case _:
                        ut.mensagem_erro('Resposta inválida. Por favor, escolha entre 1 para SIM ou 0 para NÃO.')
                        continue
    else:
        ut.mostrar_mensagem('Saindo...')

def carrinho():
    cav.carrinho()
    cpf = gt.get_cpf()
    pedidos = cam.pedidos
    if cpf in pedidos:
        pedidos_cliente = {k: v for k, v in pedidos[cpf].items() if not v[5]}  # Filtrar apenas os pedidos não pagos
        if pedidos_cliente:
            cav.carrinho2(pedidos_cliente)
            pagamentos(cpf)
        else:
            print('Nenhum pedido não pago encontrado para o CPF informado.')
    else:
        print('Nenhum pedido encontrado para o CPF informado.')
    
    print()
    input('Tecle <ENTER> para continuar...')

def pagamentos(cpf):
    pedidos = cam.pedidos
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    pedidos_cliente = pedidos.get(cpf, {})

    while True:
        resp = gt.pagamento()
        if resp in alternativas:
            break
        else:
            print('Resposta inválida. Por favor, escolha entre SIM/NÃO.')
    if resp in ['s', 'sim']:
        for pedido_id in pedidos_cliente:
            pedido = pedidos_cliente[pedido_id]
            pedido[5] = True  # Marcar como pago
    elif resp in ['n', 'nao', 'não']:
        cam.del_pedido(cpf)