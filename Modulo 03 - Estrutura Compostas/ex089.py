cadastro = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    cadastro.append([nome, [nota1, nota2], media])
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper()[0]
    if res == 'N':
        break
print('-=' * 30)
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 30)
for ind, valor in enumerate(cadastro):
    print(f'{ind:<4} {valor[0]:<10} {valor[2]:>8.1f}')

while True:
    print('-' * 30)
    para = int(input('Mostrar notas de qual alunos: (999 interrope):'))
    if para == 999:
        break
    if para <= len(cadastro) -1:
        print(f'Notas de {cadastro[para][0]} são {cadastro[para][1]}')
print('-' * 30)