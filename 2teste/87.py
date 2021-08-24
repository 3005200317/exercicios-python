matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coter = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{c}, {l}]: '))
print('=-' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end=' ')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print('=-' * 25)
print(f'A soma dos valores pares é {pares}')
for l in range(0, 3):
    coter += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {coter}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da sugunda linha é {maior}.')