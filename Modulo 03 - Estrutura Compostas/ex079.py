números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('número adicionado com sucesso!')
    else:
        print('Número já existe. Por favor tente novamente! ')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper()
    if res == 'N':
        break
números.sort()
print(f'Você digitou os valores {números}')