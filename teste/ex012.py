# calculador de porcentagem

n = float(input('Qual o preço do produto? R$'))
p = n - (n * 5 / 100)
print('{}O produto que custava R${} na promoçao com desconto de 5% vai custar R${}'.format('\033[4m', n, p))