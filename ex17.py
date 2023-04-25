import math
cato = float(input("Digite a medida do Cateto oposto: "))
cata = float(input('Digite a medida do Cateto Adjacente: '))
hip = math.hypot(cata, cato)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))