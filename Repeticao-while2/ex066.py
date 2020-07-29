n = 0
totn = 0
soma = 0
while n != 999:
    soma = soma + n
    n = int(input('Digite um número: '))
    if n == 999:
        break
    totn = totn + 1
   
print(f'total  de numeros: {totn}')
print(f'soma: {soma}')
