from random import randint
from time import sleep
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
lista = []
jogos = []
cont = 0
tot = 1
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= quant: 
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 4, f'SORTEANDO {quant} JOGOS', '-=' * 4)
for i, l in enumerate(jogos):
    print(f'JOGOS {i+1}: {l}')
print('-=' * 5, '< BOA SORTE >', '-=' * 5)