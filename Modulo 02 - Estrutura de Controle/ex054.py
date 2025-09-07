from datetime import date
ano = date.today().year
menor = 0
maior = 0
cont = 0
for pessoa in range(1, 8):
    date_nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = ano - date_nasc
    cont += 1
    if idade <= 21:
        menor += 1
    else:
        maior += 1
print('Das {} pessoas cadastradas, '
      '\n{} ainda não atingiram a maior idade e '
      '\n{} já são maiores.'.format(cont, menor, maior))