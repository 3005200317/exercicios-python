n1 = int(input('Me diga um número qualquer: '))
par = n1 % 2
if par == 0:
    print('O número {} é {}PAR{}!!'.format(n1, '\033[31m', '\033[m'))
else:
    print('O número {} é {}íNPAR{}!!'.format(n1, '\033[36m', '\033[m'))