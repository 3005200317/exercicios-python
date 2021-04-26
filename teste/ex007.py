n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A media entre {} e {} é igual a {:.1f}'.format(n1, n2, m))
if m <= 60:
    print('Sua nota tem que melhorar!! ')
else:
    print('Sua nota esta boa, PARABENS!! ')