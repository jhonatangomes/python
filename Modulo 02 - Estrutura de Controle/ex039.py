from datetime import date
nasc = int(input('Ano de nascimento: '))
data = date.today().year
idade = data - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, data))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    novo = 18 - idade
    ano = data + novo
    print('Ainda faltam {} anos para o alistamento'.format(novo))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    novo = idade - 18
    ano = data - novo
    print('Você deveria ter se alistado há {} anos'.format(novo))
    print('Seu alistamento foi em {} anos'.format(ano))