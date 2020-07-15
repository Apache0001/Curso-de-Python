frase = str(input('Digite uma frase: ')).strip().upper()
palavras =  frase.split()
junto = ''.join(palavras)

inverso = ''
for i in range(len(junto)-1, -1 , -1):
    inverso += junto[i]

if junto == inverso:
    print('A frase é um palindromo')

else:
    print('Nao e um palindromo')
