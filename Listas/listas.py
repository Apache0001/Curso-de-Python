num = []
posnum=[]

while True:
    print('------- Adicionando Números a Lista----------')
    n1 = int(input('Digite um número: '))
    if(n1 == 999):
        break
    num.append(n1)
for c in range(0,len(num)):
    if 2 in num:
        num.remove(2)

print(num)