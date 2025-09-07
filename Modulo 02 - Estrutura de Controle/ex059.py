from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
maior = 0
opção = 0
while opção != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ''')
    opção = int(input('>>>> Qual é a sua opção? '))
    print('=-' * 20)
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior entre {} e {} é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os dados novamente')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida!')
    print('=-' * 20)
    sleep(1)
print('Fim')