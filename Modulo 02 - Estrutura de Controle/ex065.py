res = 'S'
cont = soma = maior = menor = quant = 0
while res in 'Ss':
    num = int(input('Digite um número: '))
    res = str(input('Quer continuar? [S/N] '))
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        else:
            menor = num
    cont += 1
média = soma / cont
print('Você digitou {} números e a média é {}'.format(cont, média))
print('O maior valor é {} e o menor é {}'.format(maior, menor))