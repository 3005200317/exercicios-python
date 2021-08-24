print('-' * 40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)
soma = cont = maisbar = contmais1 = 0
nomepro = ' '
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    soma += preço
    if preço >= 1000:
        contmais1 += 1
    if cont == 1 or preço < maisbar:
        nomepro = prod
        maisbar = preço
    soun = ' '
    while soun not in 'SN':
        soun = str(input('Quer continuar: [S/N]')).upper().strip()[0]
    print('=' * 40)
    if soun == 'N':
        break
print('-' * 12, 'FIM DO PROGRAMA', '-' * 12)
print(f'O total da compra deu R${soma:.2f}')
print(f'Temos {contmais1} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomepro} que custa R${maisbar:.2f}')