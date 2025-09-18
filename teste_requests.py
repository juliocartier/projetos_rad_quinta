import requests

response = requests.get('https://api.adviceslip.com/advice')
print("Ola Mundo", response.json())

# 1. Caso não tenha o git instalar o git
# 2. Criar ambiente virtual do python
#   2.1 python -m venv nome_ambiente
# 3. Ativar ambiente virtual
#   3.1 source nome_ambiente/Scripts/activate
# 4. Criar arquivo em python .py
# 5. Instalar a biblioteca requests -> pip install requests
# 6. Realizar requisição da api
# 7. Para executar o arquivo em python, basta dar o comando
#   7.1 python nome_arquivo.py