n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2 
print('tirando {:.1f} é {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m <= 5.0:
    print('O aluno esta REPROVADO!')
elif m < 6.9:
    print('O aluno esta de RECUPERAÇÃO!')
else:
    print('O aluno esta APROVADO!')