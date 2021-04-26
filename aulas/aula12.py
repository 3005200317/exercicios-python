nome = str(input('Qual seu nome? '))
if nome == 'ana julia':
    print('Seu nome é bem conhecido.')
elif nome == 'pietra' or nome == 'monigia' or nome == 'sophia':
    print('Seu nome é bem diferenciado!')
elif nome == 'samuel' or nome == 'gabriel' or nome == 'miguel':
    print('Seu nome é igual de um anjo.')
else:
    print('Seu nome é bem, normal')
print('Tenha um Bom Dia, {}!!'.format(nome))