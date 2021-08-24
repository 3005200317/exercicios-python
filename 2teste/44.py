print('==' * 10, 'Supermercado', '==' * 10)
n = float(input('Preço das compras: '))
print('''Forma de pagamento
[ 1 ]A vista dinheiro/cheque
[ 2 ]A vista cartão
[ 3 ]2X no cartão
[ 4 ]3X ou mais no cartão ''')
opcao = int(input('Qual e sua opção? '))
if opcao == 1:
    por = n - (n * 10 / 100)
    print(f'Sua compra de R${n:.2f} vai custar R${por:.2f} no final')
elif opcao == 2:
    por = n - (n * 5 / 100)
    print(f'Sua compra de R${n:.2f} vai custar R${por:.2f} no final com desconto de 5%')
elif opcao == 3:
    vezes = n / 2
    print(f'Sua compra será parcelada em 2x de R${vezes:.2f}')
elif opcao == 4:
    n1 = int(input('Quantas parcelas? '))
    fica = n / n1
    sera = fica + (fica * 20 / 100)
    total = n + (n * 20 / 100)
    print(f'Sua compra será parcelado em {n1}x de R${sera:.2f} com juros')
    print(f'Sua compra de R${n:.2f} vai custar R${total:.2f} no final')
else:
    print('OPÇAO INVALIDA TENTE NOVAMENTE')