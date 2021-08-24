n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o ultimo número: '))
lista = (n1, n2, n3, n4)
print(f'Você digitou os valores {lista}')
print(f'O valor 9 aparece {lista.count(9)} vazes')
if 3 in lista:
    print(f'O valor 3 aparece na {lista.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nem uma posição')
print(f'Os valores pares digitados foram', end=' ')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
print('\n')