num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('-=' * 20)
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('Não foi digitado nenhum valor 3')
print(f'OS valores pares digitados foram ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
