precos = [200, 100, 500, 600]
#with open("precos_roupas.txt", "w") as arquivo:
#    for preco in precos:
#        arquivo.write(str(preco) + '\n')

lista_telefone = [{"nome": "Julio", "Enderecos": "Rua A", "Telefone": "12348312"},
         {"nome": "Veronica", "Enderecos": "Rua B", "Telefone": "12234832"},
         {"nome": "Murillo", "Enderecos": "Rua C", "Telefone": "13213489"},
         {"nome": "Carolina", "Enderecos": "Rua D", "Telefone": "88213481"}]

with open("lista_telefonica.txt", "w") as arquivo:
    arquivo.write("nome ; enderecos ; telefone. \n")
    for lista in lista_telefone:
        formato_lista = lista["nome"] + " ; " + lista["Enderecos"] + " ; " + lista["Telefone"]
        arquivo.write(formato_lista + '. \n')
    arquivo.close()
