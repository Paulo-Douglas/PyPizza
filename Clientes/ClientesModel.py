import libs.insertes as ins
import textwrap
import pickle

clientes = {}
try:
  arq_clientes = open("clientes.dat", "rb")
  alunos = pickle.load(arq_clientes)
except:
  arq_clientes = open("clientes.dat", "wb")
arq_clientes.close()

def salvar_clientes(clientes):
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

def chamar_dados(cpf, clientes):  # Função de formatar dados feita pela IA - GPT
    nome = clientes[cpf][0]
    endereco = clientes[cpf][1]
    
    nome_quebrado = textwrap.fill(nome, width=45)
    endereco_quebrado = textwrap.fill(endereco, width=64)
    
    linhas_nome = nome_quebrado.split('\n')
    linhas_endereco = endereco_quebrado.split('\n')
    
    max_linhas = max(len(linhas_nome), len(linhas_endereco))
    nome_final = nome
    endereco_final = endereco
    
    for i in range(max_linhas):
        nome_final = linhas_nome[i] if i < len(linhas_nome) else ''
        endereco_final = linhas_endereco[i] if i < len(linhas_endereco) else ''
    
    return nome_final, endereco_final

def alt_decisao(cpf, clientes):
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    while True:
        decisao = input('Qual dado você deseja alterar? - Tecle 0 caso não queira fazer alteração: ').lower()
        match decisao:
            case '0':
                break
            case '1':
                nome = ins.insert_name()
                clientes[cpf][0] = nome
                print('Nome alterado com sucesso.')
            case '2':
                novo_cpf = ins.insert_cpf()
                clientes[novo_cpf] = clientes.pop(cpf)
                cpf = novo_cpf
                print('O CPF foi alterado com sucesso.')
            case '3':
                endereco = ins.insert_address()
                clientes[cpf][1] = endereco
                print('O endereço foi alterado com sucesso.')
            case _:
                print('Número informado não é válido. Escolha entre: 1 (Nome), 2 (CPF) e 3 (Endereço).')
                continue

        while True:
            resp = input('Deseja fazer uma nova alteração (sim/não) ? ').lower().strip()
            if resp not in resposta:
                print('Resposta inválida. Responda com somente SIM ou NÃO.')
                continue
            if resp in ['n', 'nao', 'não']:
                print('Alterações feitas com sucesso!!')
                return

def del_cliente(cpf, clientes):
    resposta = ['s', 'sim', 'n', 'nao', 'não']
    while True:
        resp = input('Caro cliente, realmente deseja excluir sua conta do sistema (sim/não)? ').lower()
        if resp not in resposta:
            print('Resposta inválida. Responda somente com SIM ou NÃO.')
            continue
        if resp in ['s', 'sim']:
            try:
                del clientes[cpf]
                print('Exclusão bem-sucedida. Até mais.')
            except KeyError:
                print('CPF não encontrado. Nenhuma exclusão realizada.')
        else:
            print('Operação de exclusão cancelada.')
        break