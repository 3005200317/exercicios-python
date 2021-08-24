n = float(input('Qual é o slario do funcionario? R$'))
p = n + (n * 15 / 100)
print(f'Um funcionario que ganhava {n} com 15% de aumento, passa a ganhar R${p:.2f}')