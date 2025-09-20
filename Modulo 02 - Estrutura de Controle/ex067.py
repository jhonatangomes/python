while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for c in range(1, 11):
        res = num * c
        print(f'{num} x {c} = {res}')
print('Progama finalizado! Volte sempre!')