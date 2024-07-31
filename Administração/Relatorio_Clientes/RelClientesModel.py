import Clientes.ClientesModel as clm
import textwrap

clientes = clm.clientes

def chamar_dados_cliente(ativos=True):
    dados_formatados = []
    separador = '|---------------------------------------------|-----------------|-----------------------------------------------------------------|'
    
    for cpf, dados in clientes.items():
        if dados[2] == ativos:  # Verifica se o estado de atividade corresponde ao solicitado
            nome = dados[0]
            endereco = dados[1]

            nome_quebrado = textwrap.fill(nome, width=30)
            endereco_quebrado = textwrap.fill(endereco, width=60)

            linhas_nome = nome_quebrado.split('\n')
            linhas_endereco = endereco_quebrado.split('\n')

            max_linhas = max(len(linhas_nome), len(linhas_endereco))
            for i in range(max_linhas):
                cpf_final = '{:^17}'.format(cpf if i == 0 else '')
                nome_final = '{:^45}'.format(linhas_nome[i]) if i < len(linhas_nome) else '{:^45}'.format('')
                endereco_final = '{:^65}'.format(linhas_endereco[i]) if i < len(linhas_endereco) else '{:^65}'.format('')
                linha = f'|{nome_final}|{cpf_final}|{endereco_final}|'
                dados_formatados.append(linha)
            dados_formatados.append(separador)  # Linha separadora
    
    # Verificação para caso não haja clientes no estado solicitado
    if not dados_formatados:
        estado = 'ativo' if ativos else 'inativo'
        dados_formatados.append(f'Nenhum cliente encontrado com o estado {estado}.')

    return dados_formatados
