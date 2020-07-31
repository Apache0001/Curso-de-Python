#PALPITE MEGASENA
from random import randint

lista = []
while True:
    sort = randint(0, 61)
    if not sort in lista:
        lista.append(sort)
    
    if len(lista) == 6:
        break
print(lista)