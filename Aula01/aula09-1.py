nome = "Pablo Oliveira Mesquita".upper() #coloca toda  string em CAPS

print('PABLO' in nome)

nome.replace('PABLO','Gabriel') #Substitui uma palavra por outra

print(nome)

frase = "Curso em vídeo python"

print(frase.title()) # title coloca toda palavra em maiuscula

frase2 = "Curso em video"
print(frase2)
print(frase2.strip()) # Remove espaços a esquerda e a direita da string
print(frase2.strip().split()) # Coloca toda palavra em uma lista como se fosse um ventor
print('-'.join(frase2))
print(frase.count("o")) # Conta quantas vezes a letra apareceu


teste = "asduhasduhashudahsudasp"

print(teste[5::2])

print("""Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.""")
