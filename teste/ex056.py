somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    s = str(input('Sexo [F/M]: ')).strip()
    somaidade += idade
    if p == 1 and s in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if s in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if s in 'Ff' and idade < 20:
        mulher += 1
mediaidade = somaidade / 4 
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher)) 