from time import sleep
num = int(input('Digite um número: '))
print('=' * 15)
for cont in range (1, 11):
    '''res = num * cont
    print(' {} x {} = {}'.format(num, cont, res))'''
    print(' {} x {} = {}'.format(num, cont, num * cont))
    sleep(0.5)
print('=' * 15)