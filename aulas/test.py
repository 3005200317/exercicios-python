soma = 0
cont = 0
for c in range(2, 500, 2):
    if c % 2 == 0:
        soma = soma + c # acumula os valores, vai somando todos
        cont= cont + 1 # conta mais 1, mais um que eu achei
print(f'A soma de todos os {cont} valores é {soma}')
'''end=' ' # fica na mesma linha'''