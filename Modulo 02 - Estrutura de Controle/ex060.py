'''from math import factorial
f = factorial(5)
n = int(input('Digite um número para calcular'
              'seu Fatorial: '))
print('O fatorial de {} é {}'.format(n, f))'''

'''n = int(input('Digite um número para calcular'
'seu Fatorial: '))
c = n
f = 1
print('Calculando o fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))'''



n = int(input('Digite um número para calcular'
'seu Fatorial: '))
c = n
f = 1
print('Calculando o fatorial de {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else' = ', end='')
    f = f * c
print('{}'.format(f))