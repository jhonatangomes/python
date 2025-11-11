'''from time import sleep
from random import randint
print('-' * 30)
print('JOGO NA MEGA SENA')
print('-' * 30)
lista = list()
jogos = list()
quantidade = int(input('Quantos jogos você quer que eu sortei? '))
total = 1
while total <= quantidade:
    counter = 0
    while True:
        numero = randint(0, 60)
        if numero not in lista:
            lista.append(numero)
            counter += 1
        if counter >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'jogo {i + 1}: {l}')
    sleep(.5)'''

from time import sleep
from random import randint
print('-' * 30)
print(f'{'JOGO NA MEGA SENA':^30}')
print('-' * 30)
lista = list()
jogos = list()
quantidade = int(input('Quantos jogos você quer que eu sortei? '))
total = 1
while total <= quantidade:
    counter = 0
    while True:
        numero = randint(0, 60)
        if numero not in lista:
            lista.append(numero)
            counter += 1
        if counter >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' *3, ' SORTEANDO JOGOS ', '-=' *3)
for i, l in enumerate(jogos):
    print(f'jogo {i + 1}: {l}')
    sleep(.5)
print(f'{' Boa Sorte ':=^30}')