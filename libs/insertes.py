import libs.validation as val
import libs.verify as verf
import libs.get as gt

def insert_name():
    name = gt.get_name()
    while not (val.name_validator(name)):
        print('O nome informado não é válido. Por favor, informe outro!')
        name = gt.get_name()
    return name.title()

def insert_cpf():
    while True:
        cpf = gt.get_cpf()
        if not (val.cpf_validator(cpf)):
            print('O CPF informado não é válido. Por favor, informe um novo CPF.')
            continue
        if verf.verificar_cpf(cpf):
            print('O CPF informado já está cadastrado no nosso sistema. Por favor, informe um novo CPF.')
            continue
        return cpf

def insert_address():
    while True:
        endereco =  input('Informe seu endereço: ')
        return endereco

########################################### VENDAS ####################################################################

def insert_name_pizza(cardapio):
    while True:
        name = gt.get_nome_pizza()
        if val.name_validator(name):
            if any(name == detalhes[0] for detalhes in cardapio.values()):
                print('Essa pizza já está cadastrada no cardápio. Por favor, informe uma nova pizza.')
                continue
            return name

def insert_value():
    while True:
        valores = gt.get_valor()  
        if all(val.isfloat(valor) for valor in valores):
            return [float(valor) for valor in valores]  
        else:
            print('O valor informado é inválido. Por favor, informe somente números.')
            continue

def insert_ingredientes():
    ingredientes = []
    alternativas = ['s', 'sim', 'n', 'nao', 'não']
    while True:
        ing = gt.get_ingredientes()
        if val.name_validator(ing):
            ingredientes.append(ing)
            print("Ingredientes até agora:", ' - '.join(ingredientes))
        else:
            print("Ingrediente inválido. Tente novamente.")

        while True:
            resp = input("Deseja adicionar outro ingrediente? (sim/não): ").strip().lower()
            if resp in alternativas:
                break
            print('Resposta inválida. Por favor, escolha entre SIM ou NÃO.')

        if resp in ['n', 'nao', 'não']:
            print('Ingredientes foram adicionados com sucesso.')
            break
    return ingredientes

