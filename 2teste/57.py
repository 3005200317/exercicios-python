sex = str(input('Informe seu sexo: [M/F]: ')).upper().strip()[0]
while sex not in 'MnFf':
    sex = str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print(f'Sexo {sex} registrado com sucesso')
