s = str(input('Informe seu sexo: [F/M] ')).upper().strip()[0]
while s not in 'MmFf':
    s = str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(s))