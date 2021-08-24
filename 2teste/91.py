from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados:')
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = []
for k, v in jogo.items():
    print(f'{k} tirou {v} no dedo.')
    sleep(0.5)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for p, v in enumerate(ranking):  
    print(f'{p+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.5)