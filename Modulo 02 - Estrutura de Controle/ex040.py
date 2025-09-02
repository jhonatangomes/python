n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média é {:.1f}.'.format(n1, n2, media))
if media < 5:
    print('Aluno REPROVADO!')
elif media >= 5 and media < 7:
    print('Aluno em RECUPERAÇÃO!')
elif media > 7:
    print('Aluno APROVADO')