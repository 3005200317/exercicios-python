n1 = float(input('Qual é a velocidade atual do carro? '))
multa = (n1-80) * 7
if n1 > 80:
    print('{}MULTADO{}! Você excedeu o limite permitido que é de 80km/h'
    'Voce deve pagar uma multa de R${:.2f}'.format('\033[31m', '\033[m', multa))
    print('Tenha um bom dia digija com segurança! ')
else:
    print('Tenha um bom dia! dirija com segurança! ' ) 
    