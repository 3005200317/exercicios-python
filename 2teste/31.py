via = float(input('qual a distancia da sua viagem? '))
print(f'voce esta preste a começar uma viagem de {via}km')
if via <= 200:
    preço = via * 0.50
else:
    preço = via * 0.45
print(f'o preço da sua passagem sera de {preço:.2f}')