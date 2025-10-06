valores = []
impar = []
par = []
'''while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    re = ' '
    while re not in "SN":
        re = str(input('Quer continuar? [S/N] ')).upper()[0]
    if re == 'N':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')'''

while True:
    valores.append(int(input('Digite um número: ')))
    re = ' '
    while re not in "SN":
        re = str(input('Quer continuar? [S/N] ')).upper()[0]
    if re == 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')