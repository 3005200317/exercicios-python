import math
n1 = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(n1))
c = math.cos(math.radians(n1))
t = math.tan(math.radians(n1))
print('O ângulo de {} tem o SENO de {:.2f}'.format(n1, s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(n1, c))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(n1, t))