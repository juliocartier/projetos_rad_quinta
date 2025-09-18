import requests

resposta = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3550308%7C1501402/distritos")
print(resposta.status_code)

print(resposta.json())