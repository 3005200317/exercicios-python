n = str(input('Digite uma frase: '))
nome = n.split()
junto = ''.join(nome)
inverso = ''
for l in range(len(junto) -1, -1, -1):
    inverso += junto[l]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('TEMOS um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')