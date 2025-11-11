'''listA = list()
listB = list()
for linha in range(0, 3): #para cada linha
    for coluna in range(0, 3): # para cada coluna em cada linha
        listB.append((int(input(f'Digite um valor para {linha} e {coluna}: '))))
    listA.append(listB[:])
    listB.clear()
for i in listA:
    print(i)'''

matriz = [[0, 0 , 0], [0, 0 , 0], [0, 0 , 0],]
for linha in range(0, 3): #para cada linha
    for coluna in range(0, 3): # para cada coluna em cada linha
        matriz[linha][coluna] = int(input(f'Digite um valor'
                                          f' para {linha} e {coluna}: '))
for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f'[{matriz[linha][coluna]:^5}]', end='')
        print()