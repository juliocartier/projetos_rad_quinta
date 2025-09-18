# arquivo = open("teste.txt")
# print("Arquivo aberto ", arquivo)
with open("teste.txt", "r") as arquivo:
    texto = arquivo.read()
    print(texto)

with open("exemplo.txt", "w+")  as arquivo2:
    arquivo2.write("Olá mundo \n")
    arquivo2.write("Bem vindo ao python \n")

    arquivo2.seek(0)

    conteudo = arquivo2.read()
    print(conteudo)
    arquivo2.close()