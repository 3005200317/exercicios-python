galera = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    soun = ' '
    while soun not in 'SN':
        soun = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if soun == 'N':
        break
print('-=' * 25)
print(f'Ao todo você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {maior}Kg. peso de', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. peso de', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()