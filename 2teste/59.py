from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''Opcões:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    op = int(input('>>>> Qual sua opção? '))
    sleep(1.0)
    if op == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif op == 2:
        multi = n1 * n2
        print(f'O resultado de {n1} X {n2} é {multi}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        if n1 < n2:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif op == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. tente novamente')
    print('-=' * 15)
sleep(1.0)
print('Fim do programa!!')