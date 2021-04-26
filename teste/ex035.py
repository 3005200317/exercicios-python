print('-=-' * 20)
print('Analisador de triângulos.')
print('-=-' * 20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima {}NÃO{} PODEM FORMAR triângulo!'.format('\033[31m', '\033[m'))