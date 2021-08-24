from sistema import *
from arquivo import *
from time import sleep

arq = 'curso.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com secesso!')
else:
    print('Aquivo não encontrado!')
    criarArquivo(arq)

while True:
    resposta = menu(['\033[35mVer pessoas cadastradas\033[m', '\033[35mCadastrar nova pessoa\033[m', '\033[35mSair do sistema\033[m'])
    if resposta == 1:
        escreva('Opção 1')
    elif resposta == 2:
        escreva('Opção 2')
    elif resposta == 3:
        escreva('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)