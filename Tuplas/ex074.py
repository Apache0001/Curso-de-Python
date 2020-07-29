import random
numeros = (random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100))


maior = numeros[0]
menor = numeros[0]

for c in range(0, 5):
    if maior > numeros[c]:
        maior = numeros[c]
    if menor < numeros[c]:
        menor = numeros[c]
print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')

    
