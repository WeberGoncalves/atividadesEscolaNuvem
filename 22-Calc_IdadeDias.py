"""def idadeEmDias():
    while True:
        idade = input("Digite quantos anos você tem: ")
        if idade.isdigit():
            dias = int(idade) * 365
            break
        else:
            print("Erro: Digite apenas números.\n")
    return dias        

# Chamando a função corretamente
idadDdias = idadeEmDias()
print(f"Você viveu aproximadamente {idadDdias} dias.")"""

def idade_em_dias():
    while True:
        ano_nascimento = input("Digite seu ano de nascimento: ")
        if ano_nascimento.isdigit():
            ano_atual = 2025  # Pode ser atualizado com datetime.date.today().year
            idade = ano_atual - int(ano_nascimento)
            dias_vividos = idade * 365
            return dias_vividos
        else:
            print("Erro: Digite um ano válido.\n")

# Chamando a função corretamente
idade_dias = idade_em_dias()  # Nome correto da variável
print(f"Você viveu aproximadamente {idade_dias} dias.")