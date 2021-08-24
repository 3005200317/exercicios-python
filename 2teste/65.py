n = cont = media = tot = maior = menor = 0
con = ''
while con != 'N':
    n = int(input('Digite um número: '))
    con = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    media += n
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
tot = media / cont
print(f'você digitou {cont} numeros e a media foi {tot:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')