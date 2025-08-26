'''#import math
from math import trunc
num = float(input('Digite um valor: '))
#n = math.trunc(num)
n = trunc(num)
print('O valor digitado foi {}'
      ' e a sua porção inteira é {}'.format(num, n))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {}'
      ' e a sua porção inteira é {}'.format(num, int(num)))