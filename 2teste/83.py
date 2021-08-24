expr = str(input('Digite a expressão: '))
anali = []
for símb in expr:
    if símb == '(':
        anali.append('(')
    elif símb == ')':
        if len(anali) > 0:
            anali.pop()
        else:
            anali.append(')')
            break
if len(anali) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')