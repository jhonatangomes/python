from PyInstaller.compat import is_darwin

pessoa = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(pessoa)
#print(pessoa['nome'])
#print(pessoa['idade'])
#print(f'O {pessoa['nome']} tem {pessoa['idade']} anos.')
#print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.')
#print(pessoa.keys()) #mostra as chaves
#print(pessoa.values()) #mostra os valores
#print(pessoa.items()) #mostra os valores e itens


'''for k in pessoa.keys(): #mostra as chaves 
    print(k)'''

'''for v in pessoa.values():  #mostra os valores
    print(v)'''


#del pessoa['sexo'] #apaga o item
#pessoa['nome'] = 'Leandro' #modificar item
#pessoa['peso'] = 98.5 #adicionar

'''for k, v in pessoa.items():
    print(f'{k} = {v}')''' # mostra os valores e chaves


'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)'''

#print(brasil[0])
#print(brasil[1])
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
#print(brasil)
'''for e in brasil:
    print(e)'''
'''for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')'''

for e in brasil:
    for v in e.values():
        print(v, end=' - ')

    print()