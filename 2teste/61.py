print('Gerador de PA')
print('=-' * 15)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
c = pri
while cont <= 10:
    print(f'{c} -> ', end='')
    c += razao
    cont +=1
print('Fim')