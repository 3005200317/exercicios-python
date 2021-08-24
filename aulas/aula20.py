'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(3, 2)
soma(b=3, a=2)'''

'''
def titulo(t):
    print('-=' * 15)
    print(t)
    print('-=' * 15)


titulo('A historia')'''

def contador(* num):
    for valor in num:
        print(f'{valor}',end=' ')
    print('FIM')

contador(2, 4 ,6)
contador(0, 4)
contador(3, 7, 10)

'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')


contador(2, 4 ,6)
contador(0, 4)
contador(3, 7, 10)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1 


valores = [3, 5, 1, 0]
dobra(valores)
print(valores)'''