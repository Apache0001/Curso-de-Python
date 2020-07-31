lista = []
listapar = []
listaimpar = []
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)

listapar.sort()
listaimpar.sort()

lista = listapar + listaimpar

print(f'Os valores totais são: {lista}')
print(f'Os valores pares são: {listapar}')
print(f'Os valores impares são: {listaimpar}')
    
