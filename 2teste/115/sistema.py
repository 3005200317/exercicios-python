'''from time import sleep

def linha(txt):
    print('-' * 40)
    print(f'{txt:^40}')
    print('-' * 40)


while True:
    linha('MENU PRINCIPAL')
    print('1 - \033[35mVer pessoas cadastradas\033[m')
    print('2 - \033[35mcadastrar nova pessoa\033[m')
    print('3 - \033[35mSair do sistema\033[m')
    print('-' * 40)

    try:
        opção = int(input('\033[36mSua Opção:\033[m '))
    except (ValueError):
        print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
    else:
        if opção == 1:
            linha('Opção 1')
        elif opção == 2:
            linha('Opção 2')
        elif opção == 3:
            linha('Saindo do sistema... Até logo!')
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')'''


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um valor inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO: valor não encontrado.\033[m')
            return 0
        else:
            return n


def linha(tam = 40):
    return '-' * tam


def escreva(txt):
    print(linha())
    print(f'{txt:^40}')
    print(linha())


def menu(lista):
    escreva('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c}- {item}')
        c += 1
    print(linha())
    opção = leiaint('\033[36mSua Opção:\033[m ')
    return opção