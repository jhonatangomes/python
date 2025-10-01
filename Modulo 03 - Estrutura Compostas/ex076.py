listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Tranferidor', 25,
            'Compasso', 9.90,
            'Mochila', 120,
            'Canetas', 22.30
            )
print('-' * 40)
print('{: ^40}'.format(' LISTAGEM DE PREÇOS '))
print('-' * 40)
for lista in range(0, len(listagem)):
    if lista % 2 == 0:
        print(f'{listagem[lista]:.<30}', end='')
    else:
        print(f'R${listagem[lista]:>7.2f}')