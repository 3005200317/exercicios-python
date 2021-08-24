n = str(input('digite uma frase: ')).lower().strip()
l = n.count('a')
f = n.find('a') + 1
r = n.rfind('a') + 1
print(f'a letra A aparece {l} vezes na frase.')
print(f'a primeira letra A aparece na posiçao {f}')
print(f'a ultima letra A aparece na posiçao {r}')