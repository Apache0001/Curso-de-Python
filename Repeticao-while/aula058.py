import random

n =  int(input('Digite um número [0,10]: '))
sorteado = random.randint(0, 11)
tentativas = 1
while n != sorteado:
    n =  int(input('Digite um número [0,10]: '))
    tentativas = tentativas +1

print('Você acertouuu!!!')
print(f'Seu número foi {n} e você precisou de {tentativas} tentativas')
