peso = float(input('Digite seu peso: (Kg)'))
altura = float(input('Digite sua altura: (m)'))
imc = peso / (altura * altura)
print('Uma pessoa que pesa {:.1f}kg e mede {:.2f}m.'.format(peso, altura))
print('Possue um IMC de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO do Peso')
elif imc > 18.5 and imc <= 25:
    print('Você está no pesso IDEAL')
elif imc > 25 and imc <= 30:
    print('Você está com SOBREPESO')
elif imc > 30 and imc <= 40:
    print('Você está na OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')