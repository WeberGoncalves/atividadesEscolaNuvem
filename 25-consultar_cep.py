import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    #Sempre que fazemos uma requisição HTTP, recebemos um código de resposta. Um código  significa que a requisição foi bem-sucedida e os dados foram recebidos corretamente.
    if resposta.status_code == 200:
        dados = resposta.json()
        
        if "erro" in dados:
            print("CEP inválido. Tente novamente.")
        else:
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados.get('bairro', 'N/A')}")
            print(f"Cidade: {dados.get('localidade', 'N/A')}")
            print(f"Estado: {dados.get('uf', 'N/A')}")
    else:
        print("Não foi possível consultar o CEP. Verifique sua conexão.")

cep = input("Digite o CEP: ")
consultar_cep(cep)