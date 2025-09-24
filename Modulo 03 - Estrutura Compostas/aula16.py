lanche = ('hamburge', 'suco', 'pizza', 'pudim')
'''print(lanche)
print(lanche[3])
print(lanche[-3])
print(lanche[1:3])
print(lanche[-2:])'''

'''for comida in lanche:
    print(f'eu vou comer {comida}')
print('Comi pra caramba!')'''

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')'''

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
#print(c)
#print(len(c)) #saber o comprimento
print(sorted(c)) #Ordenação alfabettica
#print(c.count(5)) # saber quantas vezes tem um determinado número
#print(c.index(8)+1) #saber a posição
#print(c.index(5, 1)) #saber a posição e vai começar na 1

pessoa = ('Gustavo', 25, 'M', 99.68)
#del(pessoa)
print(pessoa)