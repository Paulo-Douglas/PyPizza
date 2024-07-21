def get_name():
    return input('Informe seu nome: ')

def get_cpf():
    return input('Informe seu CPF: ')

def get_nome_pizza():
    return input('Informe o nome da pizza: ')

def get_ingredientes():
    return input('digite o nome do ingrediente que deseja adicionar: ').title()

def get_ing_novo():
    return input('Deseja adicionar mais ingredientes (SIM/NÃO)? ').lower()

def get_valor():
    return [input(f'Digite o valor da Pizza {tamanho}. Informe somente números : ') for tamanho in ['P', 'M', 'G', 'GG']]

def get_pizza():
    return input('Digite o ID da pizza desejada: ').upper()

def get_tamanho():
    return input('Informe o tamanho da pizza (P, M, G, GG): ').lower()

def fazer_pedido():
    return input('Deseja fazer algum pedido (sim/não)? ').lower()

def get_novo_pedido():
    return input('Deseja fazer outro pedido (sim/não)? ').lower()

def pagamento():
    return input('Deseja realizar o pagamento desse(s) pedido(s) (sim/não)? ').lower()