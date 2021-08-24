n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print(f'A media entre {n1} e {n2} é igual a {m:.1f}')
if m <= 60:
    print('Sua nota tem que melhorar!! ')
else:
    print('Sua nota esta boa, PARABENS!! ')