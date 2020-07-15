#Faca um programa que sortei um valor e compare com um informado pelo usuario
# E diga se o usuario acertou.

import random

number = random.randint(0, 6)

n = int(input('Tente acertar o valor: '))

if n == number:
    print('---------------------')
    print('Você acertouu !!!')
    print('---------------------')
else:
    print('Você errou !')