'''pessoas = {'nome': 'Ana', 'idade': '18', 'sexo': 'F'}
print(pessoas)
print(pessoas.items())
print(pessoas.values())
print(pessoas.keys())
del pessoas['sexo']
pessoas['nome'] = 'julia' #adicionar ou mudar 
print(pessoas)
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k in pessoas.items():
    print(k)'''

'''brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil)'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

'''for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()'''

