d = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
total = (d * 60) + (km * 0.15)
#totald = d * 60
#totalkm = km * 0.15
#total = totald + totalkm
print('O total a pagar é de R${:.2f}'.format(total))