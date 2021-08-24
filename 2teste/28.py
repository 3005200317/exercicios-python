import random
print('=--' * 19)
print('vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('=--' * 19)
jog = int(input('em que numero eu pensei? '))
print('PROCESSANDO...')
lista = [1, 2, 3, 4, 5]
com = random.choice(lista)
if jog == com:
    print('PARABENS! voce conseguiu me vencer!')
else:
    print(f'GANHEI! eu pensei no numero {com} nao no {jog}')