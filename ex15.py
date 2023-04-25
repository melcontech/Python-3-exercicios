diaria = int(input('Quantos dias de aluguel ? '))
km = float(input('Quantos KM rodados ? '))
print('O valor a pagar é  R${}'.format((diaria * 60 ) + (km * 0.15)))