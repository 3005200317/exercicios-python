n1 = float(input('Primeira nora: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'tirando {n1:.1f} e {n2:.1f}, a media do aluno é {media:.1f}')
if media >= 7.0:
    print('O aluno esta, APROVADO')
elif media <= 5.0:
     print('O aluno esta, REPROVADO')
else:
    print('O aluno esta de, RECUPERAÇAO')