jogador = {}
num = []
time = []
while True:
    jogador.clear
    jogador['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    num.clear()
    for c in range(1, quant+1):
        num.append(int(input(f'   Quantos gols na partida {c}? ')))
        jogador['gols'] = num[:]
        jogador['total'] = sum(num)
    time.append(jogador.copy())
    soun = ' '
    while soun not in 'SN':
        soun = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if soun == 'N':
        break
print('-=' * 30)
print(f'{"cod nome":<3}{"gols":>15}{"total":>11}')
print('--' * 30)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<12}', end=' ')
    print()
print('--' * 30)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 pra parar) '))
    if dados == 999:
        break
    if dados > len(time):
        print(f'ERRO! Não existe jogador com codigo {dados}! Tente novamente')
    else:
        print(f' - levantamento do jogador {time[dados]["nome"]}:')
        for i, t in enumerate(time[dados]['gols']):
            print(f'   => No jogo {i+1}, fez {t} gols.')
    print('--' * 30)
print('<< VOLTE SEMPRE >>')