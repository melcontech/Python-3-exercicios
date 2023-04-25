import datetime
ano = int(input('Digite o Ano que você quer saber ?! Coloque zero para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}, é um ano bissexto .'.format(ano))
else:
    print('{}, não é um ano bissexto'.format(ano))