def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.2f}m².')


print('Controle de terreno')
print('-' * 20)
lar = float(input('Largura: (m) '))
com = float(input('Comprimento: (m) '))
area(lar, com)