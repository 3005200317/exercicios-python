n = float(input('Qual o preço do produto? R$: '))
pro = n - (n * 5 / 100)
print(f'O produto que custa R${n}, na promoçao com desconto de 5% vai custar R${pro:.2f}')