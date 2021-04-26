# print('\033[0;30;41m Ola mundo\033[m')

'''a = 8
b = 2
print('Os valores sao \033[37;44m{}\033[m e \033[36m{}\033[m.'.format(a, b))
'''
cores = {'limpa':'\033[m', 
          'ciano':'\033[7;36;41m', 
          'vermelho':'\033[7;31;46m'}
n = 'ana'
o = 'paula'
print('oque eu nao lembro eu nao devo {}{}{} {}{}{}'.format(cores['ciano'], n, cores['limpa'], cores['vermelho'], o, cores['limpa'])) 