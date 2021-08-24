print('=' * 30)
print('      10 TERMO DE UMA PA     ')
print('=' * 30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = termo + (10) * razao
for c in range(termo, cont, razao):
    print(f'{c}')
print('ACABOU')