soma = cont = 0
while True:
    n = int(input('Digite uma valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}:')