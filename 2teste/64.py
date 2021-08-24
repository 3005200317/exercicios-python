soma = cont = n = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
        cont += 1
        soma += n
        n = int(input('Digite um número [999 para parar]: '))
print(f'você digitou {cont} números e a soma entre eles foi {soma}')