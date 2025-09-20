from random import randint
ponto = 0
print('=-'  * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint (0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total de {total}. ', end= '')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            ponto += 1
        else:
            print('Você perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            ponto += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAME OUVER! Você venceu {ponto} vezes.')

