from math import sqrt, ceil
import random 
num  = int(input("Digite um número: "))
raiz  = sqrt(num)
print(ceil(raiz))

vetor = []
for c in range(0, 10):
    num2 = random.randint(0, 11)
    vetor.append(num2)
print(vetor)
maior = vetor[0]
menor =  vetor[0]
pmaior = 0
pmenor = 0
posMaior = []
posMenor = []

for i in range(0, 10):
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]

for i in range(0, 10):
    if maior == vetor[i]:
        posMaior.append(i)
    if menor == vetor[i]:
        posMenor.append(i)

print(f'O maior valor é: {maior} na posicão: {posMaior}')
print(f'O menor valor é: {menor} na posição: {posMenor}')

num = ['Pedra','Papel', 'Tesoura']

escolha = random.choices(num)
print(escolha)
