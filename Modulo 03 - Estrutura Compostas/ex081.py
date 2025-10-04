valor = []
c = 0
while True:
    valor.append(int(input('Digite um valor: ')))
    c += 1
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper()[0]
    if res == 'N':
        break
valor.sort(reverse= True)
print(f'Você digitou {c} elementos')
print(f'Os valores em ordem descrescente são {valor}')
if 5 in valor:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado!')