peso = int(input('Qual é seu peso? (Kg) '))
altura =float(input('Qual é sua altura? (m) '))
imc = peso / altura ** 2
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉMS, você esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você esta na faixa de SOBREPESO')
elif 30 <= imc < 40:
    print('Você está na faixa de OBESIDADE')
else:
    print('Você está na faixa de OBESIDADE MÓRBIDA, cuidado')