nome = str(input('Digite o seu nome : '))
separado = nome.split()
print('Primeiro : {}'.format(separado[0]))
print('Ultimo : {}'.format(separado[len(separado) - 1]))