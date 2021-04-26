o = float(input('comprimento do cateto oposto: '))
a = float(input('comprimento do cateto adjacente: '))
s = (o ** 2 + a ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(s))