import random
num = int(input('Adivinhe o número entre 0 e 5: '))
n = 5#random.randint(0,5)
print('O numero sorteado foi {}'.format(n))
if num == n:
    print('\033[0:33mParabéns! você ganhou')
else:
    print('\033[0:31mVocê perdeu')