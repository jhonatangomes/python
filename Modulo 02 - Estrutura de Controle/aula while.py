'''for c in range(1, 5):
    n = input('Digite um número: ')
print('FIM')'''

'''n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('FIM')'''

'''cont = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]')).upper()
    cont += 1
print('FIM', cont)'''


n = 1
cont = 0
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    cont += 1
print('Você digitou {} no total e {} são pares e {} são ímpares'.format(cont, par, impar))