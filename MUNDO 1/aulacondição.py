## condição - if / else
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Parabens, você foi aprovado !')
else:
    print('Desculpe, você está de recuperação !')