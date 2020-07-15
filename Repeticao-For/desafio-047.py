# NÚMEROS PARES EM UM INTERVALO
inicio = int(input('Digite o número inicia: '))
fim  = int(input('Digite o fim do intervalo: '))

for i in range(inicio, fim):
    if i % 2 == 0:
        print(i)


        