n1 = float(input('Qual é a distancia da sua viagem? '))
print('Você está preste a começar uma viagem de {}km.'.format(n1))
if n1 <= 200:
    preço = n1 * 0.50
else:
    preço = n1 * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))