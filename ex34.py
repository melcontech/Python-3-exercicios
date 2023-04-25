salario = float(input('Digite o seu salário: '))
if salario <= 1250:
    print('Você receberá R${:.2f} de aumento'.format(salario * 0.15))
else:
    print('Você receberá R${:.2f} de aumento'.format(salario * 0.10))