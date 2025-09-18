try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo nao encontrado.")
finally:
    print("Finalizando....")