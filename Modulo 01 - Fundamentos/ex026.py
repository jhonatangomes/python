frase = str(input('Digite uma frase: ')).strip().upper()
print('A lestra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira lestra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))