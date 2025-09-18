armazenar_dados = ("Banana", "Maçã", 10, 50, "Banana")

# print(armazenar_dados)

# armazenar_dados[0] = "Laranja"

contar = armazenar_dados.count("Banana")
# print(contar)

dicionario_valores = {"nome": ["Flavia", "Julio", "Claudiney", "Veronica"],
                      "telefone": 12345678,
                      "endereco": "Rua A",
                      "curso": "Curso A"}
print(dicionario_valores["nome"], dicionario_valores["nome"])

for chave, valor in dicionario_valores.items():
    print("Aquiii e for", chave, valor)
    if chave == 'nome':
        for valores_nome in valor:
            print("Nome = ", valores_nome)

dicionarios = {"nomes": {"nome": ["Julio", "Veronica", "Flavia", "Claudiney"]},
               "telefones": {"telefone": [1223412, 938373, 18273,81273]},
               "enderecos": {"endereco": ["Rua A", "Rua B", "Rua C", "Rua D"]}
              }

for chaves, valores in dicionarios.items():
    print("Primeiro for somente valores = ", valores)
    for index, valor in valores.items():
        print("Segundo for somente valores = ", valor)
        for valores_vetor in valor:
            print("terceiro for = ", valores_vetor)

'''dicionario_mais_de_um_valor = [{"nome": "Julio", 
                                           "telefone": 12345678,
                                           "endereco": "Rua A"},
                                {"nome": "Rafael", 
                                           "telefone": 1212348,
                                           "endereco": "Rua B"},
]

for valores in dicionario_mais_de_um_valor:
    print(valores["nome"], valores["endereco"])

'''