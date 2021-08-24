print('=' * 30)
print('{:^30}'.format('BANCO DA JU'))
print('=' * 30)
cont50 = cont20 = cont10 = cont1 = 0
sacar = int(input('Que valor você quer sacar? R$'))
while True:
    while sacar - 50 >= 0:
        sacar -= 50
        cont50 += 1
    while sacar - 20 >= 0:
        sacar -= 20
        cont20 += 1
    while sacar - 10 >= 0:
        sacar -= 10
        cont10 += 1
    while sacar - 1 >= 0:
        sacar -= 1
        cont1 += 1
    break
if cont50 != 0:
    print(f'Total de {cont50} células de R$50')
if cont20 != 0:
    print(f'Total de {cont20} células de R$20')
if cont10 != 0:
    print(f'Total de {cont10} células de R$10')
if cont1 != 0:
    print(f'Total de {cont1} células de R$1')
print('=' * 30)
print('Volte sempre ao BANCO JU! Tenha um bom dia!')