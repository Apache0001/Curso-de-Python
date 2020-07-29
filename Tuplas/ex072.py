n = ('Um','Dois','Tês')

while True:
    n1 = int(input(('Digite um número entre 0 e 20: ')))
    while n1 < 0 or n1 > 20 :
        n1 = int(input('Por favor  digite um numero entre 0 e 20: '))

    break

print(n[n1-1])

