try:
    with open("arquivo_protegido.txt", "r") as arquivo:
        arquivo.read()
        # arquivo.write("Testeeee")
except PermissionError as e:
    print(f"Erro, voce nao tem permissao para gravar. {e}")