n1 = int(input(':'))
n2 = int(input(':'))
n3 = int(input(':'))

if n1 > n2 and n1 > n3:
    print(f'Maior numero é: {n1}')
elif n2 > n3 and n2 > n1:
    print(f'Maior número é: {n2}')
else:
    print(f'Maior número é: {n3}')
