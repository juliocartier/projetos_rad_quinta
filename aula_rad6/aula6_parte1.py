def verificar_idade(idade):
    if idade < 18:
        raise ValueError("Idade não permitada")
    return "Acesso permitido"

try:
    print(verificar_idade(17))
except ValueError as e:
    print(f"Erro {e}")