import os

try:
    with open("texto.txt", "r") as arquivo:
        leitura_arquivo = arquivo.read()
        print(leitura_arquivo)
except FileNotFoundError as e:
    print("Arquivo inexistente")

try:
    os.remove("texto.txt")
    print("Apagando o arquivo que existe no nosso projeto")
except FileNotFoundError as e:
    print("Arquivo inexistente")
    print(e)