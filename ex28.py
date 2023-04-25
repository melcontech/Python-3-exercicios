import random
escolhido = random.randint(0, 5)
print('+=+'* 20)
print('         Aguarde Estou pensanso em um numero: ')
print('+=+'* 20)
usuario = int(input('Tente advinhar o numero de 0 a 5 : '))
if usuario == escolhido:
    print('YOU WIN')
else:
    print('YOU LOSE')