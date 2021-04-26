n = float(input('Qual é o slario do funcionario? R$'))
p = n + (n * 15 / 100)
print('Um funcionario que ganhava {} com 15% de aumento, passa a ganhar R${:.2f}'.format(n, p))