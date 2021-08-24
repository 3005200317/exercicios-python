casa = float(input('valor da casa: R$'))
salario = float(input('salario do comprador: R$'))
finan = int(input('quantos anos de financiamento? '))
pes = casa / (finan * 12)
mini = salario * 30 / 100
print(f'para pagar uma casa de R${casa:.2f} em {finan} anos a prestaçao sera de {pes:.2f}')
if mini <= salario:
    print('emprestimo NEGADO!')
else:
    print('emprestimo pode ser CONCEDIDO!')
    