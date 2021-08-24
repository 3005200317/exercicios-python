mais18 = maisnova = homens = 0
while True:
    print('-' * 24)
    print('  CADASTRE UMA PESSOA')
    print('-' * 24)
    idade = int(input('Idade: '))
    gen = ' '
    while gen not in 'FM':
        gen = str(input('Genero: [F/M] ')).upper().strip()[0]
    if idade >= 19:
        mais18 += 1
    if gen == 'F':
        if idade <= 20:
            maisnova += 1
    if gen == 'M':
        homens += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if opção == 'N':
        break
print('-=' * 20)
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {maisnova} mulher com menos de 20 anos.')