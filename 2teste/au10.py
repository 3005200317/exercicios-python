n1 = float(input('qual foi sua primeira nota: '))
n2 = float(input('qual foi sua segunda nota: '))
m = (n1 + n2) / 2
print(f'sua media foi {m:.2f}')
if m >= 6.0:
    print('PARABENS!')
else:
    print('TEM Q MELHORAR')