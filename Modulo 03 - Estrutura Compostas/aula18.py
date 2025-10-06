'''teste = list()
teste.append('gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 23
galera.append(teste[:])
print(galera)
'''

'''galera = [['João', 19],['Ana', 32],['Joaquim', 13],
          ['Maria', 45]]
'''#print(galera[0]) #mostra  ['João', 19]
#print(galera[0][0]) #mostra ['João']
#print(galera[2][1]) #mostra [13]'''

'''for p in galera:
    print(p)
    '''

'''for p in galera:
    print(p[0]) # só o nome
    '''

'''for p in galera:
    print(p[1])# só a idade
    '''

'''for p in galera:
    print(f'{p[0]} tem {p[1]} ano de idade.')
    '''

galera = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')