sexo = input('Digite seu Sexo [M/F]: ').upper()

while sexo != 'M' and sexo != 'F':
    print('Sexo não reconhecido! ')
    print('Por favor, Digite novamente:')
    sexo = input('Sexo [M/F]').upper()
