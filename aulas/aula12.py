nome = str(input('Qual seu nome? '))
if nome == 'ana julia':
    print('Seu nome é bem conhecido.')
elif nome == 'pietra' or nome == 'monigia' or nome == 'sophia':
    print('Seu nome é bem diferenciado!')
elif nome in 'samuel gabriel miguel':
    print('Seu nome é igual de um anjo.')
else:
    print('Seu nome é bem, normal')
print(f'Tenha um Bom Dia, {nome}!!')