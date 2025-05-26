"""
    Verifica se o texto contém apenas letras.
    Parâmetros:
    - texto (str): A entrada do usuário.
    Retorna:
    - True se o texto for válido, False caso contrário.
    """
def e_texto(texto: str):
    texto_limpo = texto.strip().lower()
    if texto_limpo.isalpha():  # Verifica se há apenas letras
        return True
    else:
        print("Erro: Digite apenas letras!")
        return False

def e_palindromo(texto: str):
    return texto == texto[::-1]  # Compara com sua versão invertida

while True:
    try:
        palavra = input("Digite uma palavra: ").strip()
        if e_texto(palavra):  # Chama a função para validar o texto
            if e_palindromo(palavra):
                print(f"{palavra} é um palíndromo.")
            else:
                print(f"{palavra} não é um palíndromo.")
            break  # Encerra o loop após uma entrada válida
    except Exception as erro:
        print(f"Erro inesperado: {erro}. Tente novamente.\n")
        