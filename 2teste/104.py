print('--' * 20)
def leiaint(le):
    while True:
        n = str(input(le))
        if n.isnumeric():
            print(f'Você acabou de digitar o número {n}')
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro valido\033[m')


# Programa principal
n = leiaint('Digite um número: ')
