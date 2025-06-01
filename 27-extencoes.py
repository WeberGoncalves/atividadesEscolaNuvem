import os

def identificar_extensao(arquivo):
    _, extensao = os.path.splitext(arquivo)#Separa o nome do arquivo e sua extensão
    return extensao.lower()

def ler_arquivo(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as dado:
            print(dado.read())
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def escrever_arquivo(arquivo):
    texto = input("Digite o texto para escrever no arquivo: ")
    with open(arquivo, "w", encoding="utf-8") as dado:
        dado.write(texto)
    print("Texto salvo com sucesso.")

def adicionar_arquivo(arquivo):
    texto = input("Digite o texto para adicionar ao arquivo: ")
    with open(arquivo, "a", encoding="utf-8") as dado:
        dado.write("\n" + texto)
    print("Texto adicionado com sucesso.")

arquivo = input("Digite o nome do arquivo (.txt, .csv, .json): ")
extensao = identificar_extensao(arquivo)

if extensao in [".txt", ".csv", ".json"]:
    acao = input("Deseja ler, escrever ou adicionar ao arquivo? (ler/escrever/adicionar): ").strip().lower()

    if acao == "ler":
        ler_arquivo(arquivo)
    elif acao == "escrever":
        escrever_arquivo(arquivo)
    elif acao == "adicionar":
        adicionar_arquivo(arquivo)
    else:
        print("Ação inválida.")
else:
    print("Extensão não suportada.")