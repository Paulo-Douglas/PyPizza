import libs.files as fil

clientes = fil.carregar_dados('clientes.dat')

def verificar_cpf(cpf):
    return cpf in clientes

def obter_cliente(cpf):
    return clientes.get(cpf)