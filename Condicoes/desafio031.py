distancia =  float(input('Digite a distância da viagem: '))

if distancia < 200:
    print(f'O valor pago é: {distancia * 0.5}')
else:
    print(f'O valor pago é: {distancia * 0.45}')
    