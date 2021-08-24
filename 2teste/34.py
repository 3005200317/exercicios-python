n = float(input('qual o salario do funcionario? R$'))
if n >= 1250:
    sa = n + (n * 10 / 100)
if n <= 1250:
    sa = n + (n * 15 / 100)
print(f'quem ganhava R${n:.2f} passa a ganhar R${sa:.2f} agora')