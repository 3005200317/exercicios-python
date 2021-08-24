num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n1 = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n1 <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {num[n1]}') # fazer ele perguntar se quer continuar