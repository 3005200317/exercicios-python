num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    soun = ' '
    while soun not in 'SN':
        soun = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if soun == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')