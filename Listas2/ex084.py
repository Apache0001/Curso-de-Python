lista = []
linha = []
totp = 0

# ADICIONANDO VALORES A MATRIZ
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    linha.append(nome)
    linha.append(peso)
    lista.append(linha[:])
    linha.clear()
    totp += 1
    
    ask = str(input('Deseja continuar? [S/N]: ')).upper()

    if ask == 'N':
        break

maiorpeso = lista[0][1]
menorpeso = lista[0][1]
listapesoMaior = []
listapesoMenor = []

#LISTANDO O MAIOR E MENOR PESO
for p in lista:
    if p[1] >= maiorpeso:
        maiorpeso = p[1]


    if p[1] <= menorpeso:
        menorpeso = p[1]

# LISTA AS PESSOAS COM OS MAIORES PESOS!
# LISTA COM AS PESSOAS DE MENORES PESSOS!
for p in lista:
    if p[1] == maiorpeso:
         listapesoMaior.append(p[0])
    if p[1] == menorpeso:
        listapesoMenor.append(p[0])



print(f'Lista dos maiores peso ({maiorpeso}) são: {listapesoMaior}')
print(f'Lista dos menores peso ({menorpeso}) são: {listapesoMenor}')