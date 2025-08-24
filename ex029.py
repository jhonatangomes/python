vel = int(input('Qual a velocidade do carro? '))
print('A velocidade do carro é {}km/h'.format(vel))
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[31mMULTADO! Você excedeu a limite premitido que é 80km.')
    print('Você deve pagar um multa de\033[m \033[33mR${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')