print('=' * 10, 'lojas Souza', '=' * 10)
preço = float(input('preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão ou mais''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    dc = preço - (preço * 10 / 100)
    print(' Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, dc))
elif opção == 2:
    c = preço - (preço * 5 / 100)
    print(' Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, c))
elif opção == 3:
    c2 = preço / 2
    print(' Sua compra será parcelada em 2x de {:.2f} '.format(c2))
elif opção == 4:
    fi = preço + (preço * 20 / 100)
    parc = int(input('Quantas parcelas? '))
    c3 = preço / parc
    print(' Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parc, c3))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, fi))
else:
    print('''OPÇÃO INVALIDA de pagamento. tente novamente!
Sua compra de R${} vai custar R${} no final.'''.format(preço, preço))
