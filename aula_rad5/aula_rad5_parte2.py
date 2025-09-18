
with open("arquivo2.txt", "r") as arquivo:
    print("Representacao original da linha")
    for linha in arquivo:
        linha2 = linha.strip()
        print(repr(linha2))

minha_lista = ['Arroz', 'Feijao', 'Carne']
lista = ', '.join(minha_lista)
with open('produtos.txt', 'w') as arquivo:
    arquivo.write(str(minha_lista) + '\n')
    arquivo.write(lista)