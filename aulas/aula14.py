'''for c in range(10, 0, -1):
    print(c)
print('FIM')'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')'''

'''n = 1
while n != 0:
    n = int(input('Digite um numero: ')) # enquanto n digitar o 0 o codigo continua...
print('FIM')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} números pares e {impar} impares!')