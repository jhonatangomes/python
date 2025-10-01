num = []
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]

print('=-' * 30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(num):
     if num[indice] == maior:
         print(f'{indice}... ', end= '')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}... ', end='')