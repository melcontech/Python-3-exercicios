frase = str(input('Digite uma frase : ')).strip()
print('Quantas vezes aparece a letra "A" : {} vezes'.format(frase.upper().count('A')))
print('A Primeira Letra A está na {}ª posição ! '.format(frase.upper().find('A')+1))
print('A Ultima Letra A está na {}ª posição ! '.format(frase.upper().rfind('A')+1))