soma = 0
cont = 0
for num in range(1, 7):
    n = int(input('Digite o {}º número: '.format(num)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você me informou {} número pares e é {}.'.format(cont, soma))