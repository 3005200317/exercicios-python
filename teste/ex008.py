medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f'A medida de {medida}m corresponde a \n {cm:.0f}cm \n {mm:.0f}mm \n {dm:.0f}dm \n {dam}dam \n {hm}hm \n {km}km')