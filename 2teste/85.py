'''valores = []
for c in range(1, 8):
    valores.append(int(input(f'Digite o {c} valor: ')))
print('-=' * 25)
print('Os valores pares digitados foram:', end=' ')
valores.sort()
for n in valores:
    if n % 2 == 0:
        print(f'{n},', end=' ')
print()
print('Os valores ímpares digitados foram:', end=' ')
valores.sort()
for n in valores:
    if n % 2 == 1:
        print(f'{n},', end=' ')
print()'''

num = [[], []]
valores = 0
for c in range(1, 8):
    valores = int(input(f'Digite o {c} valor: '))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)
print('-=' * 25)
num[0].sort()
print(f'Os valores pares digitados foram: {num[0]}')
num[1].sort()
print(f'Os valores ímpares digitados foram: {num[1]}')