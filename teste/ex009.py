t = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    s = t * c
    print(f'{t} X {c} = {s}')
print('-' * 12)