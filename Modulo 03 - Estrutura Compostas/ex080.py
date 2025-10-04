num = []
for c in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if c == 0:
        num.append(n)
        print('Adicionado na posição 0')
    elif n > num[len(num) - 1]:
        num.append(n)
        print('Adicionado ao final da lista')
print(f'Os valores digitado foram {num}')