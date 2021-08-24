from datetime import datetime
informaçoes = {}
informaçoes['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
informaçoes['idade'] = datetime.now().year - ano
informaçoes['ctps'] = int(input('Carteira de trabalho (0 nâo tem): '))
while True:
    if informaçoes['ctps'] > 0:
        informaçoes['contratacão'] = int(input('Ano de contratacão: '))
        informaçoes['salario'] = float(input('Salário: R$'))
        informaçoes['aposentadoria'] = informaçoes['idade'] + ((informaçoes['contratacão'] + 35) - datetime.now().year)
    break
print('-=' * 20)
for k, v in informaçoes.items():
    print(f'  -{k} tem o valor {v}')