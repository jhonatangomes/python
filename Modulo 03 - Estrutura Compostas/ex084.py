cadastro = []
valores = []
maior = menor = 0
while True:
    valores.append(str(input('Nome: ')))
    valores.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        maior = menor = valores[1]
    else:
        if valores[1] > maior:
            maior = valores[1]
        if valores[1] < menor:
            menor = valores[1]
    cadastro.append(valores[:])
    valores.clear()
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper()[0]
    if res == 'N':
        break
print('-=' * 30)
print(cadastro)
print(f'Ao todo, você cadastrou {len(cadastro)} pessoas')
print(f'O maior peso foi de {maior} kg. O peso de ', end= '')
for p in cadastro:
    if p[1] == maior:
        print(f' {p[0]}' , end='')
print('')
print(f'O menor peso foi de {menor} kg. Peso de', end='')
for p in cadastro:
    if p[1] == menor:
        print(f' {p[0]}', end='')