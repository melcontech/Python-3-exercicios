import math
grau = float(input('Quantos graus: '))
sen = math.sin(math.radians(grau))
cos = math.cos(math.radians(grau))
tan = math.tan(math.radians(grau))
print('SENO {:.2f}\nCOSSENO {:.2f}\nTANGENTE {:.2f}'.format(sen, cos, tan))