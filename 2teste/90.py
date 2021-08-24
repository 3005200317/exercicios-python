valores = {}
valores['nome'] = str(input('Nome: '))
valores['media'] = float(input(f'Média de {valores["nome"]}: '))
print('-=' * 12)
if valores['media'] <= 5.0:
    valores['situaçao'] = 'Reprovado'
elif valores['media'] <= 7.0:
    valores['situaçao'] = 'Recuperaçao'
else:
    valores['situaçao'] = 'Aprovado'
for k, v in valores.items():
    print(f'{k} é igual a {v}')