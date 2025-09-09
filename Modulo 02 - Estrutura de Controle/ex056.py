'''p = cont = 0
soma = velho = 0
for p in range(1, 5):
    print(('-' * 5 + ' {}ª PESSOA '+'-' * 5).format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] ')).strip().upper()
    if sexo == 'M':
        if idade > velho:
            velho = idade
            homem = nome
    soma += idade
    if sexo == 'F' and idade < 20:
        cont += 1
media = soma / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, homem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont))'''



p = cont = soma = velho = 0

for p in range(1, 5):
    print(('-' * 5 + ' {}ª PESSOA '+'-' * 5).format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] ')).strip().upper()
    if p == 1 and sexo in 'Mm':
        velho = idade
        homem = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        homem = nome
    if sexo in 'Ff' and idade < 20:
        cont += 1
    soma += idade
media = soma / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, homem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont))