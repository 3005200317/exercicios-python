# com cores do guanabara
'''from time import sleep

c = ('\033[m',    # limpa 0
    '\033[0;42m', # verde 1
    '\033[0;41m', # vermelho 2
    '\033[0;44m', # azul 3
    '\033[7;30m') # branco 4

def ajuda(com):
    escreva(f"Acessando o manual do comando \'{fun}\'", 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def escreva(txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    escreva('SISTEMA DE AJUDA PyHELP', 1)
    fun = str(input('Função ou biblioteca > '))
    if fun.upper() == 'FIM':
        break
    else:
        ajuda(fun)
escreva('ATÉ LOGO!', 2)'''

# o meu sem cores
from time import sleep

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

while True:
    escreva('SISTEMA DE AJUDA PyHELP')
    print()
    fun = str(input('Função ou Biblioteca > '))
    print()
    if fun != 'fim':
        escreva(f"Acessando o manual do comando '{fun}'")
        sleep(1)
        help(fun)
    if fun == 'fim':
        break
escreva('ATÉ LOGO')