jogador = {}
num = []
jogador['nome'] = str(input('Nome do jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, quant):
    num.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = num[:]
    jogador['total'] = sum(num)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {quant} partidas.')
for i, t in enumerate(num):
    print(f'   => Na partida {i}, fez {t} gols.')
print(f'Foi um total de {jogador["total"]} gols.')