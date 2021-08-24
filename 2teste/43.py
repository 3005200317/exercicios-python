peso = int(input('Qual seu peso? Kg '))
altura = float(input('Qual sua altura? m '))
imc = peso / altura ** 2
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('voce esta na faixa ABAIXO do peso')
elif 18.5 <= imc < 25:
    print('voce esta na faixa do peso IDEAL')
elif 25 <= imc < 30:
    print('voce esta na faixa do SOBREPESO')
elif 30 <= imc < 40:
    print('voce esta na faixa da OBESIDADE')
else:
    print('voce esta na faixa da OBESIDADE MÓRBIDA')