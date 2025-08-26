num = int(input('\033[35mMe diga um número qualquer: '))
if num % 2 == 0:
    print('\033[37mO numero {} \033[34mPAR'.format(num))
else:
    print('\033[37mO numero {} \033[34mIMPAR'.format(num))