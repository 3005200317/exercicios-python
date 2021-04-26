casa = float(input('Valor da casa: R$'))
salario = float(input('Sálario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
Prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('a prestação será R${:.2f}'.format(Prestação))
if Prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')