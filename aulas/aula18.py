'''teste = list()
teste.append('ana julia')
teste.append('18')
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['joao', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

'''galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')'''