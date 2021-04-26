n1 = float(input('Quantos dias foi alugado? '))
n2 = float(input('Quantos km rodado? '))
c = n1 * 60
r = n2 * 0.15
print('O total a pagar é de R${:.2f}'.format(c + r))