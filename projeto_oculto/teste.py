clientes = {
    "123.456.789-10": "João Silva",
    "987.654.321-00": "Maria Oliveira",
    "456.789.123-20": "Carlos Santos"
}

cardapio = {
    1: {
        "nome": "Pizza de Calabresa",
        "ingredientes": ["mussarela", "calabresa", "cebola", "azeitona", "molho de tomate"],
        "valor": 35.90
    },
    2: {
        "nome": "Pizza de Frango com Catupiry",
        "ingredientes": ["mussarela", "frango desfiado", "catupiry", "milho", "molho de tomate"],
        "valor": 39.90
    },
    3: {
        "nome": "Pizza Margherita",
        "ingredientes": ["mussarela", "tomate", "manjericão", "azeite", "molho de tomate"],
        "valor": 33.90
    }
}

def exibir_cardapio():
    print('----------------------------------------------')
    print('|                   Cardápio                 |')
    print('----------------------------------------------')
    cpf = input('Informe seu cpf: ')
    if cpf in clientes:
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|                                                     Cardápio                                                                    |')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        print('|   ID   |       Nome       |                            Ingredientes                             |             Valores           |')
        print('|---------------------------------------------------------------------------------------------------------------------------------|')
        for id, item in cardapio.items():
            nome = item["nome"]
            ingredientes = ', '.join(item["ingredientes"])
            valores = item["valor"]
            print(f"|   {id}   |   {nome}   |   {ingredientes}   |   {valores}   |")


exibir_cardapio()