import controller.ClientesController as clc
import libs.files as fil
import libs.insertes as ins
import libs.get as gt
import textwrap

clientes = fil.carregar_dados('clientes.dat')

def chamar_dados(cpf):
    if cpf not in clientes:
        return None, None
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
                nome = ins.insert_name()
                clientes[cpf][0] = nome
                print('Nome alterado com sucesso.')
            elif decisao == 'cpf':
                novo_cpf = ins.insert_cpf()
                clientes[novo_cpf] = clientes.pop(cpf)  # Atualiza a chave
                cpf = novo_cpf  # Atualiza o valor de cpf
                print('O CPF foi alterado com sucesso.')
            else:
                endereco = ins.insert_address()
                clientes[cpf][1] = endereco
                print('O endereço foi alterado com sucesso.')
        else:
            print('Dado informado não existe. Escolha entre: NOME, CPF e ENDEREÇO.')
            continue
            
        resp = input('Deseja fazer uma nova alteração (sim/não) ? ').lower()
        if resp not in resposta:
            print('Resposta inválida. Responda com somente SIM ou NÃO.')
            continue
        if resp in ['n', 'nao', 'não']:
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
                fil.salvar_clientes(clientes)
                print('Exclusão bem-sucedida. Até mais.')
            except KeyError:
                print('CPF não encontrado. Nenhuma exclusão realizada.')
        else:
            print('Operação de exclusão cancelada.')
        break