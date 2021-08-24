cadastro = {}
galera = []
soma = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        if cadastro['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    galera.append(cadastro.copy())
    while True:
        soun = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if soun in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')  
    if soun == 'N':
        break
print('-=' * 30)
print(f' - O grupo tem {len(galera)} pessoas.')
média = soma / len(galera)
print(f' - A média de idade é de {média:.2f} anos.')
print(f' - As mulheres cadastradas foram:', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f' - Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')