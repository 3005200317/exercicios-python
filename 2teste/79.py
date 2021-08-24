valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    soun = ' '
    while soun not in 'SN':
        soun = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if soun == 'N':
        break
print('-=' * 20)
valores.sort()
print(f'Você digitou os valores{valores}')