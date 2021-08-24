import random
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
com = random.choice(lista)
acer = False
palpi = 0
jog = 0
while jog != com:
    jog = int(input('Qual seu palpite? '))
    palpi += 1
    if jog == com:
        acertou = True
    else:
        if jog < com:
            print('Mais...Tente mais uma vez')
        elif jog > com:
            print('Menos...Tente mias uma vez')
print(f'Acertou com {palpi} tentativas. Parabéns!')