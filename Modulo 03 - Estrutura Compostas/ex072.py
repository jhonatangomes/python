num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessente', 'dezoito',
       'dezenove', 'vinte')

while True:
    valor = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= valor <= 20:
        break
    print('Tente novamente!... ', end='')
print(f'Você digitou o número {num[valor]}')