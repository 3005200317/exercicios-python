# minha resolução

'''print('Gerador de PA')
print('=-' * 15)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
c = pri
while cont <= 10:
    print(f'{c} -> ', end='')
    c += razao
    cont +=1
print('Pausa')
while mais != 0:
    mais = int(input('Quantos termos você quer mostrar a mais? ')
        cont+= mais
        print(f'Progressão finalizada com {cont -1} termos mostrados.')'''

# resolução guanabara
print('Gerador de PA')
print('=-' * 15)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
c = pri
mais = 10
tot = 0
while mais != 0:
    tot += mais
    while cont <= tot:
        print(f'{c} -> ', end='')
        c += razao
        cont +=1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    print(f'Progressão finalizada com {tot} termos mostrados.')