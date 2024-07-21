import os

def clear_screen():
    os.system('clear || cls')

def mostrar_mensagem(mensagem):
    print(mensagem)
    print()
    input('Tecle <ENTER> para continuar...')

def mensagem_erro(mensagem):
    print(mensagem)