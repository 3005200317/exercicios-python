valores = []
for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da listra...')
                break
            pos += 1
print('-=' * 26)
print(f'Os valores digitados em ordem foram {valores}')