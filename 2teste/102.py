print('--' * 20)
def fatorial(fat, show=False):
    """
    -> calcula o  fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) mostra ou não a conta
    return: o valor do fatorial de um número n
    """
    f = 1
    for c in range(fat, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# programa principal
print(fatorial(5, show=True))
# help(fatorial)