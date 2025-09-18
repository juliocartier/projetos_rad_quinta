texto = "Ola pessoal, estou salvando essa frase em um arquivo"
outra_frase = "Bem vindo pessoal, e uma nota do aluno"

with open("arquivo_exemplo.txt", 'w') as arquivo:
    arquivo.write(texto + '\n')
    arquivo.write(outra_frase)

with open("texto2.txt", 'w+') as arquivo2:
    arquivo2.write(texto)
    # print(arquivo2.read())

with open("texto2.txt", 'r') as arquivo3:
    #arquivo2.write(texto)
    print(arquivo3.read())