casa = float(input('Qual o valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
ano= int(input('Quantos anos de financiamento? '))
prestação = casa / (ano * 12)
mini = sal * 30 / 100
print('Para pegar uma casa de {:.2f} em {} anos a prestação '
      'será de R${:.2f}'.format(casa, ano, prestação))
if prestação <= mini:
    print('Empréstimo Concedido!')
else:
    print('Empréstimo não concedido!')