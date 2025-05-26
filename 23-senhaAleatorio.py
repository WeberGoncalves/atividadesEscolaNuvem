import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #ascii_letters=Retorna todas as letras do alfabeto (maiúsculas e minúsculas)
    # digits= Retorna todos os dígitos numéricos de 0 a 9.
    #punctuation= Retorna todos os caracteres especiais e símbolos de pontuação.
    senha = ''.join(random.choices(caracteres, k=tamanho))
    return senha

def pergunta():
    try:
        senha_teste = gerar_senha(int(input("Qual tamanho da senha? ")))
        return print("Senha: {}".format(senha_teste))
    except:
        print("O valor deve ser um número")
        return pergunta()

pergunta()