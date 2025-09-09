print('Gerador de PA')
print('-=' * 10)

num = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = num
cont  = 1
while cont <= 10:
    print('{} -> '.format(termo), end= '')
    termo += razão
    cont += 1
print('FIM')