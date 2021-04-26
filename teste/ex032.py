from datetime import date
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'ciano':'\033[36m'}
ano = int(input('Que ano quer analisar? Coloque 0 para ver o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}O ano de {} é bissexto'.format(cores['ciano'], ano))
else:
    print('{}O ano de {} {}nao{} {}é bissexto'.format(cores['ciano'], ano, cores['vermelho'], cores['limpa'], cores['ciano']))
