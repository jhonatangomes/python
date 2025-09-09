print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
num = int(input('Quantos termos quer mostrar? '))
c = 3
t1 = 0
t2 = 1
t3 = 1
print('~' * 5 * num)
print('{} -> {} ->'.format(t1, t2), end= '')
while c <= num:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
