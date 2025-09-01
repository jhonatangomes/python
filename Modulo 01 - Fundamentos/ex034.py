sal = float(input('Digite o valor do salário: R$'))
if sal < 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('O salário atual é de R${:.2f} com o aumento ficou em R${:.2f}'.format(sal, novo))