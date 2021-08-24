'''num = [5, 4, 7, 6]
num[1] = 2 # troca o 4 pelo 2
num.append(0) # adiciona no final da lista
num.sort() # tamanho decrescente
num.insert(1, 9) # adicona o 9 depois da possiçao 1
if 0 in num:
    num.remove(0)
else:
    print('esse numero n tem na lista')
print(num)
print(f'Esta lista tem {len(num)} elementos')'''

'''valores = []
valores.append(4)
valores.append(9)
valores.append(2)
for c, v in enumerate(valores):
    print(f'na posiçao {c} emcontrei o valor {v}')
print('cheguei ao final da lista')'''

'''valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posiçao {c} emcontrei o valor {v}')
print('cheguei ao final da lista')'''

'''a = [2, 5, 9, 0]
b = a[:]
b[2] = 1
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

from random import randint
from time import sleep
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
lista = []
jogos = []
tot = 0
quant = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
            



print('-=' * 20)
for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')