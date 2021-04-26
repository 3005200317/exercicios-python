l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
t = (l * a) /2
print('Sua parede tem a dimensão {}x{} e sua area é de {}m²'.format(l, a, (l*a)))
print('Para pintar essa parede, vc precisara de {}l de tinta.'.format(t))