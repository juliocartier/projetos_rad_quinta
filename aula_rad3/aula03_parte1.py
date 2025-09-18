adicionar_palavra = []
while(True):
    print("----------Menu-----------")
    print("OPCAO 1: INSERIR PALAVRA")
    print("OPCAO 2: LISTAR PALAVRAS")
    print("OPCAO 3: DELETAR PALAVRA POR INDICE")
    print("OPCAO 4: ATUALIZAR PARA UMA NOVA PALAVRA")
    print("OPCAO 5: PARAR PROGRAMA")
    opcao = int(input("Digite a opcao (1, 2, 3, 4, 5) = "))
    if opcao == 1:
        palavra = input("Digite a palavra para adicionar: ")
        adicionar_palavra.append(palavra)
    elif opcao == 2:
        print("Listar Palavras: ")
        print(adicionar_palavra)
    elif opcao == 3:
        posicao = int(input("Digite a posicao da palavra: "))
        del adicionar_palavra[posicao]
    elif opcao == 4:
        posicao = int(input("Digite a posicao que deseja alterar."))
        nova_palavra = input("Digite a nova palavra: ")
        adicionar_palavra[posicao] = nova_palavra
    elif opcao == 5:
        break
    else:
        print("Voce digitou uma opcao invalida.")
        break
else:
    print("Fim do programa")

