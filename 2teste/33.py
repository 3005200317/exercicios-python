n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
n3 = int(input('terceiro valor: '))
menor = n1 
if n1 < n2 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'o menor valor digitado foi {menor}')
maior = n1
if n1 > n2 and n2 < n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'o maior valor digitado foi {maior}')