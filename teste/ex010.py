real = float(input('Quanto dinheiro vc tem na carteira? R$'))
dolar = real / 5.40
euro = real / 6.43
print('Com R${:.2f} vc pode comprar US${:.2f}'.format(real, dolar))
print('com R${:.2f} vc pode comprar EUR${:.2f}'.format(real, euro))
