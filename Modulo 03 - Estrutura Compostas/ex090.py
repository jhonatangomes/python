cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['media'] = float(input(f'Media de {cadastro["nome"]}: '))
if cadastro['media'] >= 7:
    cadastro['situação'] = 'Aprvado'
elif cadastro['media'] < 7:
    cadastro['situação'] = 'Recuperação'
else:
    cadastro['situação'] = 'Reprovado'
print('-=' * 30)
print(f'Nome é igual a {cadastro["nome"]}')
print(f'Média é igual a {cadastro["media"]}')
print(f'A situação é igual a {cadastro["situação"]}')