lista = []
while True:
    n = int(input('Digite um valor: '))
    resp = str(input('Deseja continuar [S/N]')).upper()
   

    if (n in lista):
       print('Número ja está na lista') 
    else:
        lista.append(n) 
    
    if resp == 'N':
        break
lista.sort()
print(lista)