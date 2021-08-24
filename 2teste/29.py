v = float(input('qual a velocidade atual do carro? '))
m = (v-80) * 7
if v > 80:
    print('MULTADO! voce excedeu o limite permitido q e de 80km/h')
    print(f'voce deve pagar uma multa de R${m}!')
print('Tenha um bom dia! dirija com segurança!')