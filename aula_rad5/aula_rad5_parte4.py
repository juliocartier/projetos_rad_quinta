try:
    while(True):
        try:
            numero = int(input("Digite um numero: "))
            resultado = 10/numero
            print(f"Resultado = {resultado}")
            parar_programa = input("Deseja parar o programa: Sim/Nao.")
            if (parar_programa == 'Sim'):
                break
        except ValueError:
            print("Erro: Voce deve digitar um numero inteiro")
        except ZeroDivisionError:
            print("Erro: Nao é possivel dividir por zero")
        except Exception as e:
            print(f"Erro inesperado: {e}")
finally:
    print("Finalizando....")