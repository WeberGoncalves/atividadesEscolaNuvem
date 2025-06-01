"""EXERCÍCIO PRÁTICO 4
Crie um programa que consulte a cotação atual de uma moeda
estrangeira em relação ao Real Brasileiro (BRL). O usuário deve
informar o código da moeda desejada (ex: USD, EUR, GBP), e o
programa deve exibir o valor atual, máximo e mínimo da
cotação, além da data e hora da última atualização. Utilize a
API da AwesomeAPI para obter os dados de cotação."""

import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        
        chave_moeda = f"{moeda}BRL"
        if chave_moeda in dados:
            info = dados[chave_moeda]
            print(f"Moeda: {info['name']}")
            print(f"Valor atual: R$ {info['bid']}")
            print(f"Valor máximo: R$ {info['high']}")
            print(f"Valor mínimo: R$ {info['low']}")
            print(f"Última atualização: {info['create_date']}")
        else:
            print("Código da moeda inválido. Tente novamente.")
    else:
        print("Não foi possível consultar a cotação. Verifique sua conexão.")

moeda = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(moeda)