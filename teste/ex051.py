print('==' * 15)
print('     10 TERMOS DE UMA PA')
print('==' * 15)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: ')) # tem q ser diferente de zero
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('ACABOU')