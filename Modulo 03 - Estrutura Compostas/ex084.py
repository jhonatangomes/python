lista = list()
prin = list()
totmaior = totmenor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Peso: ')))
    if len(prin) == 0:
        totmaior = totmenor = lista[1]
    else:
        if lista[1] > totmaior:
            totmaior = lista[1]
        if lista[1] < totmenor:
            totmenor = lista[1]
    prin.append(lista[:])
    lista.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? ')).upper()[0]
    if resposta == 'N':
        break
print(f'Ao todo, foram cadastrada {len(prin)} pessoas')
print(f'O maior peso foi de {totmaior:.2f}kg. Peso de ', end='')
for p in prin:
    if p[1] == totmaior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {totmenor:.2f}kg. Peso de ', end='')
for p in prin:
    if p[1] == totmenor:
        print(f'{p[0]} ', end='')
print()

''''lista = list()
prin = list()
totmaior = totmenor = tot = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Peso: ')))
    prin.append(lista[:])
    lista.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? ')).upper()[0]
    if resposta == 'N':
        break

for ind, valor in enumerate(prin):
    if len(prin) == 0:
        totmaior = totmenor = valor[1]
    else:
        if valor[1] > totmaior:
            totmaior = valor[1]
            tot += 1
        if valor[1] < totmenor:
            totmenor = valor[1]
print(tot)
print(f'Ao todo, foram cadastrada {len(prin)} pessoas')
print(f'O maior peso foi de {totmaior:.2f}kg. Peso de ', end='')
for peso in prin:
    if peso[1] == totmaior:
        print(f'{peso[0]} ', end='')
print()
print(f'O menor peso foi de {totmenor:.2f}kg. Peso de ', end='')
for peso in prin:
    if peso[1] == totmenor:
        print(f'{peso[0]} ', end='')
print()''''
