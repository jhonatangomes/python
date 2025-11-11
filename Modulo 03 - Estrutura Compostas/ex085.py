lista = [[], []]
for num in range(1, 8):
    numero = int(input(f'Digite O {num}º valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
'''lista[0].sort()
lista[1].sort()'''
print(f'Os valores pares  digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')