cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretobranco':'\033[7;30m'}

dest = int(input('Qual é a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(dest))
if dest < 200:
        valor = dest * 0.50
else:
        valor = dest * 0.45
print('E o valor da sua passagem será de R${:.2f}'.format(valor))