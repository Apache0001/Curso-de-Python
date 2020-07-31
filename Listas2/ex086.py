m = []
for j in range(0, 3):
    linha = []
    for i in range(0,  3):
        linha.append(int(input(f'Digite o elemento A[{i}][{j}]: ')))
    
    m.append(linha[:])

print(f'Minha matrix')
for p in m:
    print(p)

#SOMANDO TODOS OS VALORES PARES
somap = 0
somac = 0
for j in range(0, 3):
    for i in range(0, 3):
        if m[j][i] % 2 == 0:
            somap += m[j][i]
for i in range(0, 3):
    somac += m[i][2]

print(f' A soma da 3 Coluna: {somac}')
print(f'A soma dos valores Pares: {somap}')