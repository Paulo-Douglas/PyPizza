import model.ClientesModel as clm
import view.ClientesView as clv
import libs.validation as val

clm.carregar_clientes()

def insert_name():
    name = clv.get_name()
    while not (val.name_validator(name)):
        print('O nome informado não é válido. Por favor, informe outro!')
        name = clv.get_name()
    return name.title()

def insert_cpf():
    while True:
        cpf = clv.get_cpf()
        if not (val.cpf_validator(cpf)):
            print('O CPF informado não é válido. Por favor, informe um novo CPF.')
            continue
        if clm.verificar_cpf(cpf):
            print('O CPF informado já está cadastrado no nosso sistema. Por favor, informe um novo CPF.')
            continue
        return cpf

def insert_cpf_check():
    while True:
        cpf = clv.get_cpf()
        if not (val.cpf_validator(cpf)):
            print('O CPF informado não é válido. Por favor, informe um novo CPF.')
            continue
        if clm.verificar_cpf(cpf):
            break

def insert_street():
    while True:
        rua = clv.get_rua()
        if val.name_validator(rua):
            return rua
        print('O nome da rua informado é inválido. Por favor, informe outro!')

def insert_number():
    while True:
        numero = clv.get_numero()
        if val.num_validator(numero):
            return numero
        print('O número informado é inválido. Por favor, informe outro usando somente números inteiros!')

def insert_neighborhood():
    while True:
        bairro = clv.get_bairro()
        if val.name_validator(bairro):
            return bairro
        print('O nome do bairro informado é inválido. Por favor, informe outro!')

def insert_address():
    street = insert_street()
    number = insert_number()
    neighborhood = insert_neighborhood()
    return {'rua': street, 'numero': number, 'bairro': neighborhood}

def register_client():
    clv.cadastrar_clientes()
    nome = insert_name()
    cpf = insert_cpf()
    endereco = insert_address()
    clm.adicionar_clientes(cpf, nome, endereco)

def dados_exibir():
    clv.exibir_dados1()
    cpf = clv.get_cpf()
    if clm.verificar_cpf(cpf):
        nome, endereco = clm.chamar_dados(cpf)
        clv.dados_clientes(cpf, nome, endereco)
    else:
        print("CPF não encontrado no sistema.")
    input('Tecle <ENTER> para continuar...')

def dados_alterar():
    clv.alterar_dados()
    cpf = clv.get_cpf()
    if clm.verificar_cpf(cpf):
        nome, endereco = clm.chamar_dados(cpf)
        clv.dados_clientes(cpf, nome, endereco)
        clm.alt_decisao(cpf)
    else:
        print('O cpf informado não está cadastrado no nosso sistema.')
    input('Tecle <ENTER> para continuar...')

def cliente_excluir():
    clv.excluir_cliente()
    cpf = clv.get_cpf()
    if clm.verificar_cpf(cpf):
        nome, endereco = clm.chamar_dados(cpf)
        clv.dados_clientes(cpf, nome, endereco)
        clm.del_cliente(cpf)
    else:
        print('O cpf informado não está cadastrado no nosso sistema.')
    input('Tecle <ENTER> para continuar...')