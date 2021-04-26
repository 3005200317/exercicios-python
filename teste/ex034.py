n1 = float(input('Qual é o salario do funcionario? R$'))
if n1 <= 1250:
    quantidade = n1 + (n1 * 15 / 100)
else:
    quantidade = n1 + (n1 * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar {:.2f} agora.'.format(n1, quantidade))