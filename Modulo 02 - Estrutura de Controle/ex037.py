num = int(input('Digite um número inteiro: '))
print('Escolha uma opção para conversão:'
      '\n[1] converter para BINÁRIO'
      '\n[2] converter para OCTAL'
      '\n[3] converter para HEXADECIMAL')
op = int(input('Sua opção: '))
if op == 1:
    print("{} convertido para BINÁRIO"
          " é igual a {}".format(num, bin(num)[2:]))
elif op == 2:
    print("{} convertido para OCTAL"
          " é igual a {}".format(num, oct(num)[2:]))
elif op == 3:
    print(print("{} convertido para HEXADECIMAL"
          " é igual a {}".format(num, hex(num)[2:])))
else:
    print('Opção invalida. Tente novamente!')