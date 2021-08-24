from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    n = int(input(f'Em que ano a {c} pessoa nasceu? '))
    ano = atual - n
    if ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maior de idade')
print(f'e tambem tivemos {menor} pessoas menor de idade')