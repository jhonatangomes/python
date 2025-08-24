preco = float(input('Qual o preço do produto? '))
desc = preco - (preco * 5 / 100)
if preco >= 50 :
    print('O produto que custava R${:.2f}, na promoção com desconto 5% vai custar R${:.2f}'.format(preco, desc))
print('Obrigado pela a compra!')