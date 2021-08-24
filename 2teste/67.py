while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    print('~' * 15)
    for c in range(1, 11):
        print(f'{tab} X {c} = {tab*c}')
    print('~' * 15)
print('PROGRAMA DE TABUADA ENCERRADO.')