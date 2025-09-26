try:
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Arquivo lido com sucesso.")
except FileNotFoundError:
    print("Arquivo nao encontrado.")
else:
    print("Conteudo do arquivo: ", conteudo)
finally:
    print("Finalizando a leitura do arquivo.")

try:
    with open("novo_arquivo.txt", "w") as arquivo:
        arquivo.write("Escrevendo no arquivo.")
        print("Arquivo criado com sucesso")
except Exception as e:
    print(f"Erro ao manipular o arquivo: {e}")
finally:
    arquivo.close()
    print("Arquivo fechado.")