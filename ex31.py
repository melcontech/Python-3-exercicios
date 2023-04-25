dist = float(input('Digite quantos km de distancia : '))
if dist <= 200:
    print('O valor da sua viagem será R${:.2f}'.format(dist * 0.5))
else:
    print('O valor da sua viagem será R${:.2f}'.format(dist * 0.45))