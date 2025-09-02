from datetime import date
ano = date.today().year
nasc = int(input('Digite sua idade: '))
idade = ano - nasc
print('sua idade {} anos'.format(idade))
if idade <= 9:
    print('Compertição MIRIM')
elif idade <= 14:
    print('Compertição INFANTIL')
elif idade <= 19:
    print('Compertição JUNIOR')
elif idade <= 25:
    print('Compertição SÊNIOR')
else:
    print('Compertição MASTER')