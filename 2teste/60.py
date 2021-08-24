n = int(input('''Digite um número para
calcular seu fatorial: '''))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end=' -> ')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

# n = int(input('''Digite um número para
# calcular seu fatorial: '''))
'''f = 1
print(f'Calculando {n}! = ', end='')
for c in range(n, 0, -1):
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
print(f'{f}')'''