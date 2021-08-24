def metade(preço = 0, form = False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar
    :param taxa: qual a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    return: o valor reajustado, com ou sem formato.
    """
    res = preço / 2
    return res if form is False else moeda(res)


def dobro(preço = 0, form = False):
    res = preço * 2
    return res if form is False else moeda(res)


def aumentando(preço = 0, taxa = 0, form = False):
    res = preço + (preço * taxa / 100)
    return res if form is False else moeda(res)


def diminuir(preço = 0, taxad = 0, form = False):
    res = preço - (preço * taxad / 100)
    return res if form is False else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço = 0, taxa = 10, taxad = 5):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{moeda(dobro(preço))}')
    print(f'Metade do preço: \t{moeda(metade(preço))}')
    print(f'{taxa}% de aumento: \t{moeda(aumentando(preço, taxa))}')
    print(f'{taxad}% de redução: \t{moeda(diminuir(preço, taxad))}')
    print('-' * 40)