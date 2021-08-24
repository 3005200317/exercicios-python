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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um valor inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO: valor não encontrado.\033[m')
            return 0
        else:
            return n
        

n1 = leiaint('Digite um inteiro: ')
n2 = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')