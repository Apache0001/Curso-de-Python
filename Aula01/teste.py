import random
lista = []
listord = []
for i in range(0, 10):
    lista.append(random.randint(0, 11))

print(lista)

for i in range(0, 10):
    for j in range(0, 10):
        if lista[i] <= lista[j]:
            menor = lista[i]
            print(menor)


