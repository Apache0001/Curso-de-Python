lista = []
for c in range(0, 5):
    lista.append(int(input('Didigite um Valor: ')))


maior = lista[0]
menor = lista[0]
posmaior = []
posmenor = []

# Buscando o maior e o menor valor da lista
for i in range(0, len(lista)):
    if lista[i] >= maior:
        maior = lista[i]
        
    if lista[i] <= menor:
        menor = lista[i]
# Descobrindo posicao(oes) do(s) valore(s) maior(es) e menor(es).
for pos, c in enumerate(lista):
    if c == maior:
        posmaior.append(pos)       
    if c == menor:
        posmenor.append(pos)
    
print(f'O maior valor da lista é: {maior} na posicao {posmaior}')
print(f'O menor vlaor da lista é: {menor} na posicao {posmenor}')