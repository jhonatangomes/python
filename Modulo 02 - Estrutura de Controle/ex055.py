p = 0
maior = menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lifo foi {}kg'.format(menor))