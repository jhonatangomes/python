matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = maior = somac = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor para'
                                          f'[{linha} e {coluna}]: '))
print('-=' * 25)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end= '')
        if matriz [linha][coluna] % 2 == 0:
            somap += matriz[linha][coluna]
    print()
print(f'A soma dos valore pares é {somap}')
for linha in range(0, 3):
    somac += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somac}')
for c in range(0, 3):
    if c == 0:
        maior= matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')