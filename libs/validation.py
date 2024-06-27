def name_validator(nome):
    nome = nome.strip() # a função strip removerá os espaços em branco do começo e final da str
    if all(caracter.isalpha() or caracter.isspace() for caracter in nome):   # A função all retornará um valor booleano: True ou False
        num_letras = sum(caracter.isalpha() for caracter in nome) # a função sum fará a suma de todas os caracteres da variável nome 
        if num_letras >= 3:
            return nome
        else:
            print('O nome informado deve ter ao menos 3 letras.')
    else:
        print('O nome de pizza informado é inválido. Informe um que possua somente letras e espaços!')


def cpf_validator(cpf):  # função para validar cpf - [GPT]
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    soma = 0
    for indice in range(9):
        soma += int(cpf[indice]) * (10 - indice)
    resto = soma % 11
    if resto < 2:
        digito_verificador1 = 0
    else:
        digito_verificador1 = 11 - resto
    if digito_verificador1 != int(cpf[9]):
        return False
    soma2 = 0
    for indice in range(10):
        soma2 += int(cpf[indice]) * (11 - indice)
    resto2 = soma2 % 11
    if resto2 < 2:
        digito_verificador2 = 0
    else:
        digito_verificador2 = 11 - resto2
    if digito_verificador2 != int(cpf[10]):
        return False
    return True

def num_validator(num):
    num = num.replace(' ', '')
    if num.isdigit():
        return num

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False