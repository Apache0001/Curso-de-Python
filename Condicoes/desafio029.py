velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    print('Você ultrapassou o limite permitido! Será multado!')
    print(f'A multa é no valor de R$ {velocidade * 7} ')