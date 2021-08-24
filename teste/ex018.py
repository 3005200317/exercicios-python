from math import radians, sin, cos, tan
n1 = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(n1))
c = cos(radians(n1))
t = tan(radians(n1))
print(f'O ângulo de {n1} tem o SENO de {s:.2f}')
print(f'O ângulo de {n1} tem o COSSENO de {c:.2f}')
print(f'O ângulo de {n1} tem o TANGENTE de {t:.2f}')