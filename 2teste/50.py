cont = 0
soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        cont += 1
        soma += n
print(f'tem {cont} valoes PARES e a soma deles é {soma}')