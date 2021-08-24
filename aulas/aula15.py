'''while True # laço infinito
     break # termina o laço'''

from random import randint

print('-=' * 15)
print('   VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
# cont = 0
while True:
    jog = int(input('Digite um valor: '))
    opcão = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    com = randint(0, 10)
    soma = jog + com
    par = soma % 2
    if par == 0:
        parouimpar = 'P'
        print('-' * 50)
        print(f'Você jogou {jog} e o computador {com}. Total deu {soma} DEU PAR')
        print('-' * 50)
        if opcão == parouimpar:
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('-=' * 15)
        else:
            print('Você PERDEU!')
            print('-=' * 15)
            break

    if par != 0:
        parouimpar = 'I'
        print('-' * 50)
        print(f'Você jogou {jog} e o computador {com}. Total deu {soma} DEU IMPAR')
        print('-' * 50)
        if opcão == parouimpar:
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('-=' * 15)
        else:
            print('Você PERDEU!')
            print('-=' * 15)
            break
print(f'GAME OVER! Você venceu {cont} vezes.')