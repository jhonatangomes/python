'''sex = 's'
while sex != 'F' and sex != 'M':
    sex = str(input('Digite seu Sexo: [M/F] ')).upper()
    if sex != 'M' and sex != 'F':
        print('Sexo Invalido. Por favor, digite novamente')
    else:
        print('=' * 10)
        print('Sexo valido!')'''

'''sex = str(input('Digite seu Sexo: [M/F] ')).upper()
while sex != 'F' and sex != 'M':
    sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
print('Sexo {} registrado com sucesso'.format(sex))
'''

sex = str(input('Digite seu Sexo: [M/F] ')).strip().upper()[0]
while sex not in 'FfMm':
    sex = str(input('Dados inválidos. '
                    'Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sex))
