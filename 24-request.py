import requests

# Faz a requisição para a API
informacao = requests.get("https://randomuser.me/api/")
resposta= informacao.json()

pessoa = resposta['results'][0]
nome = f"{pessoa["name"]["first"]} {pessoa["name"]["last"]}"
email = {pessoa["email"]}
pais = {pessoa["location"]["country"]}

print(f"Nome: {nome}\n E-mail: {email}\n País: {pais}")


   
