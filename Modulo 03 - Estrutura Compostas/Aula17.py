'''num = [2, 5, 9, 1]
num[2] = 3 # adicionar pelo o indice
num.append(7) # adicionar no final
#num.sort() # ordem
num.sort(reverse=True) #ordem reversa
num.insert(2, 2)
#num.pop(2)#apagar pelo o indice
#num.remove(2) # remove o primeiro elementos
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

#valores = []
'''valores = list()
valores.append(5)
valores.append(9)
valores.append(4)'''

'''for v in valores:
    print(f'{v}...', end='')'''

'''for c, v in enumerate(valores):
    print(f'Na possição {c + 1} encontrei o valor {v}')
print('Cheguei ao final da lista.')'''



'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na possição {c + 1} encontrei o valor {v}')
print('Cheguei ao final da lista.')
'''

''' #Muda as duas
a = [2, 3, 5, 7]
b = a
b[2] = 8
print(f'List A: {a}')
print(f'Lista B: {b}')'''


#Muda as só uma, cria copia de A
a = [2, 3, 5, 7]
b = a[:]
b[2] = 8
print(f'List A: {a}')
print(f'Lista B: {b}')