tot = totH = totM= 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        tot += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade <= 20:
        totM += 1
    if res == 'N':
        break
print(f'O total de pessoa com mais de 18 anos: {tot}')
print(f'Ao todos temos {totH} homem cadastrados')
print(f'E temos {totM} mulher com menos de 20 anos')