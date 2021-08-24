print('=' * 36)
print(f'{"LISTAGEM DE PREÇO":^36}')
print('=' * 36)
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
'''for cont in range(0, len(lista)):
    print(f'{lista[cont]}', end=' ')'''
for cont in range(0, len(lista)):
    if cont % 2 == 0:
        print(f'{lista[cont]:.<30}', end='')
    else:
        print(f'{lista[cont]:>6.2f}')
print('=' * 36)