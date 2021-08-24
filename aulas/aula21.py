'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    return: sem retorno
    """
    # docstrings
    c = 1
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

help(contador)'''

def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
# parâmetros opicionais

soma(5, 2, 3)
soma(2, 3)
soma()

'''def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
# Retorno de valores

n1 = soma(5, 2, 3)
n2 = soma(2, 3)
n3 = soma(7)
print(f'os resultados foram {n1}, {n2} e {n3}')'''

'''def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    

num = int(input('Digite um numero: '))
if par(num):
    print('È par')
else:
    print('Não é par')'''