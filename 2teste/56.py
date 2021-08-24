soma = 0
cont = 0
maioridadeh = 0
nomevelho = ''
for c in range(1, 5):
    print('-' * 5, f'{c} PESSOA', '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sex = str(input('sexo [M/F]: ')).strip()
    soma += idade / 4
    if c == 1 and sex in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sex in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sex in 'Ff' and idade <= 19:
        cont += 1
print(f'A media de idade do grupo é de {soma} anos')
print(f'O homem mais velho tem {maioridadeh} anos e se chama {nomevelho}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos')