cont = 0
tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end= '')
        cont += 1
    else:
        print('\033[31m', end= '')
    print('{} '.format(c), end= ' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('Ele é primo')
else:
    print('Não é primo')