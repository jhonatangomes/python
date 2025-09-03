from random import randint
from time import sleep
itens = ('pedra', 'papel' , 'tesoura')
computador = randint(0, 2)
#computador = 1
print('Sua opção:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
opção = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
print('-=' * 15)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[opção]))
sleep(1)
print('-=' * 15)
if computador == 0:
    if opção == 0:
        print('EMPATE')
    elif opção == 1:
        print('JOGADOR VENCEU')
    elif opção == 2:
        print('JOGADOR PERDEU')
    else:
        print('Opção invalida!')
if computador == 1:
    if opção == 0:
        print('JOGADOR PERDEL')
    elif opção == 1:
        print('EMPATE')
    elif opção == 2:
        print('JOGADOR VENCEU')
    else:
        print('Opção invalida!')
if computador == 2:
    if opção == 0:
        print('JOGADOR VENCEU')
    elif opção == 1:
        print('JOGADOR PERDEL')
    elif opção == 2:
        print('EMPATE')
    else:
        print('Opção invalida!')