n = int(input('Digite um número inteiro: '))

f = c = 1
while c <= n:
    f = f * c
    c = c + 1

print(f'O fatorial de {n} é : {f}')