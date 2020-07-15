nome = "Pablo Oliveira Mesquita"

print(nome)

pos = []

for i in range(len(nome)):
    if nome[i] == " ":
        pos.append(i)

for i in range(len(pos)):
    if i == 0:
        print(nome[0:pos[i]])
    else:
        print('\n temos que pensar')