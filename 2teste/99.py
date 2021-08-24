from time import sleep
def maior(* num):
    print('-=' * 20)
    mai = 0
    print('Analisando os valores passados...')
    tam = len(num)
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.7)
        if valor > mai:
            mai = valor
    print(f'foram informados {tam} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {mai}')
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()