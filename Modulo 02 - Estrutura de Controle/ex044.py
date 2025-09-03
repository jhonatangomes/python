print('========= LOJAS ===========')
valor = float(input('Digite o valor do produto: R$'))
print('FORMA DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    novo = valor - (valor * 10 /100)
    print('Sua compra de R${:.2f} vai custar'
          ' R${:.2f} no final.'.format(valor, novo))
elif opção == 2:
    novo = valor - (valor * 5 / 100)
    print('Sua compra de R${:.2f} vai custar'
          ' R${:.2f} no final.'.format(valor, novo))
elif opção == 3:
    novo = valor
    juros = novo / 2
    print('Sua compra será parcelada em 2x de '
          'R${:.2f} Sem juros'.format(juros))
    print('Sua compra de R${:.2f} vai custar'
          ' R${:.2f} no final.'.format(valor, novo))
elif opção == 4:
    parc = int(input('Quantas parcelas '))
    novo = valor + (valor * 20 / 100)
    juros = novo / parc
    print('Sua compra será parcelada em {}x de '
          'R${:.2f} com juros'.format(parc, juros))
    print('Sua compra de R${:.2f} vai custar'
          ' R${:.2f} no final.'.format(valor, novo))
else:
    novo = 0
    print('Opção Invalida')