from time import sleep
'''s = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        s = s + c
print(s)
'''

soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
        #soma += c
        #sleep(0.5)
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))