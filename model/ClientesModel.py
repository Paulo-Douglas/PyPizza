import controller.ClientesController as clc
import textwrap
import pickle

clientes = {}

def carregar_clientes():
    global clientes
    try:
        arq_clientes = open("clientes.dat", "rb")
        clientes = pickle.load(arq_clientes)
    except (FileNotFoundError, EOFError):
        arq_clientes = open("clientes.dat", "wb")
        pickle.dump(clientes, arq_clientes)

def salvar_clientes():
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

def adicionar_clientes(cpf, nome, endereco):
    global clientes
    clientes[cpf] = [nome, endereco]
    salvar_clientes()

def verificar_cpf(cpf):
    return cpf in clientes

def obter_cliente(cpf):
    return clientes.get(cpf)

def chamar_dados(cpf):
    nome = clientes[cpf][0]
    endereco = clientes[cpf][1]
    endereco_str = f"{endereco['rua']}, {endereco['numero']} - {endereco['bairro']}"
    
    nome_quebrado = textwrap.fill(nome, width=45)
    endereco_quebrado = textwrap.fill(endereco_str, width=64)
    
    linhas_nome = nome_quebrado.split('\n')
    linhas_endereco = endereco_quebrado.split('\n')

    max_linhas = max(len(linhas_nome), len(linhas_endereco))
    
    nome_final = []
    endereco_final = []

    for i in range(max_linhas):
        nome_final.append(linhas_nome[i] if i < len(linhas_nome) else '')
        endereco_final.append(linhas_endereco[i] if i < len(linhas_endereco) else '')
        
    return "\n".join(nome_final), "\n".join(endereco_final)

def alt_decisao(cpf):
    alternativas = ['nome', 'cpf', 'endereço', 'endereco']
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    verificar = True
    while verificar:
        decisao = input('Qual dado você deseja alterar? - Tecle 0 caso não queira fazer alteração: ').lower()
        if decisao == '0':
            break
        elif decisao in alternativas:
            if decisao == 'nome':
                nome = clc.insert_name()
                clientes[cpf][0] = nome
                print('Nome alterado com sucesso.')
            elif decisao == 'cpf':
                novo_cpf = clc.insert_cpf()
                clientes[cpf] = novo_cpf
                print('O CPF foi alterado com sucesso.')
            else:
                endereco = clc.insert_address()
                clientes[cpf][1] = endereco
                print('O endereço foi alterado com sucesso.')
        else:
            print('Dado informado não existe. Escolha entre: NOME, CPF e ENDEREÇO.')
            continue
            
        resp = input('Deseja fazer uma nova alteração (sim/não) ? ').lower()
        if resp not in resposta:
            print('Resposta inválida. Responda com somente SIM ou NÃO.')
            continue
        if resp == 'n' or resp == 'nao' or resp == 'não':
            print('Alterações feitas com sucesso!!')
            verificar = False

def del_cliente(cpf):
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    while True:
        resp = input('Caro cliente, realmente deseja excluir sua conta do sistema (sim/não)? ').lower()
        if resp not in resposta:
            print('Resposta inválida. Responda somente com SIM ou NÃO.')
            continue
        if resp in ['s', 'sim']:
            try:
                del clientes[cpf]
                salvar_clientes() 
                print('Exclusão bem-sucedida. Até mais.')
            except KeyError:
                print('CPF não encontrado. Nenhuma exclusão realizada.')
        else:
            print('Operação de exclusão cancelada.')
        break

