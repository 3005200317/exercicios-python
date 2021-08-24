from time import sleep
lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    soun = ' '
    while soun not in 'SN':
        soun = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if soun == 'N':
        break
print('-=' * 15)
print(f'{"No":<4} {"NOME":<11} MÉDIA')
print('-' * 30)
for pos, n in enumerate(lista):
    print(f'{pos:<4} {n[0]:<12} {n[2]:.1f}')
print('--' * 30)
while True:
    alu = int(input('Mostrar notas de qual aluno(a)? (999 interrompe): '))
    if alu == 999:
        break
    if alu <= len(lista) - 1:
        print(f'Notas de {lista[alu][0]} são {lista[alu][1]}')
print('--' * 30)
print('FINALIZANDO...')
sleep(0.5)
print('<<<VOLTE SEMPRE>>>')