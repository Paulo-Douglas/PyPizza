import Administração.Relatorio_Clientes.RelClientesModel as relcm
import Administração.Relatorio_Clientes.RelClientesView as relcv
import Administração.AdmModel as admm
import libs.utils as ut
import libs.get as gt

adm = admm.adm

def exibir_clientes_ativos():
    while True:
        conf = ut.confirmacao('administrador', 'a exibição dos dados dos clientes ativos')
        match conf:
            case '1':
                relcv.exibir_dados_clien_ativos()
                cpf = gt.get_cpf()
                if cpf in adm:
                    dados = relcm.chamar_dados_cliente(ativos=True)
                    relcv.dados_clientes_ativos(dados)
                    ut.mostrar_mensagem(' ')
                    break
                else:
                    ut.mostrar_mensagem('O CPF informado não está cadastrado em nosso sistema ou não pertence a um administrador.')
                    break
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro administrador, a opção informada não é válida. Por favor, digite 1 para continuar com a exibição ou 0 para sair.')
                continue

def exibir_clientes_inativos():
    while True:
        conf = ut.confirmacao('administrador', 'a exibição dos dados dos clientes inativos')
        match conf:
            case '1':
                relcv.exibir_dados_clien_inativos()
                cpf = gt.get_cpf()
                if cpf in adm:
                    dados = relcm.chamar_dados_cliente(ativos=False)  # Pede dados dos clientes inativos
                    relcv.dados_clientes_inativos(dados)
                    ut.mostrar_mensagem(' ')
                    break
                else:
                    ut.mostrar_mensagem('O CPF informado não está cadastrado em nosso sistema ou não pertence a um administrador.')
                    break
            case '0':
                break
            case _:
                ut.mensagem_erro('Caro administrador, a opção informada não é válida. Por favor, digite 1 para continuar com a exibição ou 0 para sair.')
                continue