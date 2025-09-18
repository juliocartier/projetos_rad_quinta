listas = [["Cachorro", "Gato", "Papagaio"],
          ["Carro", "Moto",   "Bicicleta"],
          [1000,     200,             10]]

print(listas[1][1])
print(listas[2][2])
print(listas)

for i in range(len(listas)):
    for j in range(len(listas)):
        print(listas[i][j])
