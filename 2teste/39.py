n = int(input('ano de nascimento: '))
print('''Escolha uma opção: 
[ 1 ]homen
[ 2 ]mulher''')
opção = int(input('Sua opção: '))
idade = 2021 - n
print(f'Quem nasceu em {n} tem {idade} anos em 2021')

if opção == 1 and idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
    
elif 18 < idade:
    falta = idade - 18 
    sera = 2021 - falta
    print(f'Voce ja deveria ter se alistado ha {falta} anos.')
    print(f'Seu alistamento foi em {sera}')

elif idade < 18:
    falta = 18 - idade 
    sera = falta + 2021
    print(f'Ainda falta {falta} anos para o alistamento')
    print(f'Seu alistamento sera em {sera}')

if opção == 2:
    print('Voce não precisa fazer o alistamento obrigatorio')
