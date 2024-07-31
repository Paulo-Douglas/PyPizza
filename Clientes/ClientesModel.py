import Clientes.ClientesView as clv
import libs.insertes as ins
import libs.insertes as ins
import libs.utils as ut
import textwrap
import pickle

clientes = {}

def carregar_clientes(): # Função adaptada pela IA -> GPT
    global clientes
    try:
        arq_clientes = open("clientes.dat", "rb")
        clientes = pickle.load(arq_clientes)
    except (FileNotFoundError, EOFError):
        arq_clientes = open("clientes.dat", "wb")
    arq_clientes.close()

def salvar_clientes():
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

def chamar_dados(cpf): # Função adaptade pela IA -> Copilot
    nome = clientes[cpf][0]
    endereco = clientes[cpf][1]
    
    nome_quebrado = textwrap.fill(nome, width=45)
    endereco_quebrado = textwrap.fill(endereco, width=60)
    
    linhas_nome = nome_quebrado.split('\n')
    linhas_endereco = endereco_quebrado.split('\n')
    
    max_linhas = max(len(linhas_nome), len(linhas_endereco))
    for i in range(max_linhas):
        nome_final = linhas_nome[i] if i < len(linhas_nome) else ''
        endereco_final = linhas_endereco[i] if i < len(linhas_endereco) else ''
    return nome_final, endereco_final

def alt_decisao(cpf):
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    while True:
        decisao = input('Qual dado você deseja alterar? - Tecle 0 caso não queira fazer alteração: ')
        match decisao:
            case '0':
                return False
            case '1':
                nome = ins.insert_name()
                clientes[cpf][0] = nome
                salvar_clientes()
                nome, endereco = chamar_dados(cpf)
                clv.alterar_dados2(cpf, nome, endereco)
                print('Nome alterado com sucesso.')
            case '2':
                novo_cpf = ins.insert_cpf()
                clientes[novo_cpf] = clientes.pop(cpf)
                cpf = novo_cpf
                salvar_clientes()
                nome, endereco = chamar_dados(cpf)
                clv.alterar_dados2(cpf, nome, endereco)
                print('O CPF foi alterado com sucesso.')
            case '3':
                endereco = ins.insert_address()
                clientes[cpf][1] = endereco
                salvar_clientes()
                nome, endereco = chamar_dados(cpf)
                clv.alterar_dados2(cpf, nome, endereco)
                print('O endereço foi alterado com sucesso.')
            case _:
                ut.mensagem_erro('Número informado não é válido. Escolha entre: 1 (Nome), 2 (CPF) e 3 (Endereço).')
                continue

        while True:
            resp = input('Deseja fazer uma nova alteração (sim/não)? ').lower().strip()
            if resp not in resposta:
                ut.mensagem_erro('Resposta inválida. Responda com somente SIM ou NÃO.')
                continue
            if resp in ['n', 'nao', 'não']:
                ut.mostrar_mensagem('Alterações feitas com sucesso!!')
                return False
            break

def del_cliente(cpf):
    while True:
        resp = ut.confirmacao('cliente', 'a exclusão da sua conta')
        match resp:
            case '1':
                if cpf in clientes:
                    clientes[cpf][2] = False
                    salvar_clientes()
                    break
                else:
                    ut.mensagem_erro('CPF não encontrado. Nenhuma exclusão realizada.')
                    break
            case '0':
                break
            case _:
                ut.mensagem_erro('Resposta informada não é válida. Escolha entre: 1 (continuar com a exclusão) e 2 (sair).')

def checar_cpf():
    while True:
        cpf = ins.insert_cpf()
        if cpf in clientes and not clientes[cpf][2]:  # Verifica se a conta está inativa
            decisao = input('Caro cliente, você possui uma conta inativa no nosso sistema. Deseja reativá-la? Digite 1 para reativá-la ou 0 para prosseguir sem reativá-la: ')
            match decisao:
                case '1':
                    clientes[cpf][2] = True  # Reativar a conta
                    ut.mostrar_mensagem('A conta foi reativada com sucesso. Para checar os dados, vá na função -> Exibir Dados.')
                    salvar_clientes()
                    return 0  # Retorna 0 para indicar que a conta foi reativada
                case '0':
                    return cpf  # Retorna o CPF para continuar o cadastro
        elif cpf in clientes and clientes[cpf][2]:  # Verifica se a conta já está ativa
            ut.mostrar_mensagem('Já existe uma conta ativa com esse CPF. Por favor, informe um novo CPF.')
            return None  # Adicionado retorno None para indicar que a conta está ativa
        else:
            return cpf
                
carregar_clientes()