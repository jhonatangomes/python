#num = int(input('Digite um número: '))
#print('O dobro de {} é {}'.format(num, (num  * 2)))
#print('E o tripo é {}'.format(num * 3))
#print('E a raiz quadrada é {}'.format(num//2))

n1 = int(input('Digite um numero: '))
#print('{} x {:2} = {}'.format(n1, 1, (n1 * 1)))
#print('{} x {:2} = {}'.format(n1, 2, (n1 * 2)))
#print('{} x {:2} = {}'.format(n1, 3, (n1 * 3)))
#print('{} x {:2} = {}'.format(n1, 4, (n1 * 4)))
#print('{} x {:2} = {}'.format(n1, 5, (n1 * 5)))
#print('{} x {:2} = {}'.format(n1, 6, (n1 * 6)))
#print('{} x {:2} = {}'.format(n1, 7, (n1 * 7)))
import time
for c in range (1, 11):
    r = n1 * c
    print('{} x {} = {}'.format(n1, c, r))
    time.sleep(0.5)