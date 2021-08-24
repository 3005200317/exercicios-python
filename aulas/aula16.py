lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche[0:2])

for cont in range(0, len(lanche)):
    print(f'Eu quero comer {lanche[cont]} na possiçao {cont}')
    
'''for pos, comida in enumerate(lanche):
    print(f'Eu quero comer {comida} na possiçao {pos}')
print('Que vontade')'''

# sem mostra a possiçao

for cont in range(0, len(lanche)):
    print(f'Eu quero comer {lanche[cont]}')

'''for comida in lanche:
    print(f'Eu quero comer {comida}')
print('Que vontade')'''

# print(sorted(lanche)) coloca em ordem