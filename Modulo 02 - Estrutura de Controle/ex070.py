print('-' * 40)
print('{: ^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)
total = maiorM =  cont = barato = 0
nome = ' '
while True:
    nomeP = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        maiorM += 1
    cont += 1
    if cont == 1:
        barato = preco
        nome = nomeP
    else:
        if preco < barato:
            barato = preco
            nome = nomeP
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total de compra foi de R${total:.2f}')
print(f'Temos {maiorM} de produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${barato:.2f}')