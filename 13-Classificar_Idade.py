def classificar_idade():
    idade = int(input("Digite sua idade: "))
    
    if idade < 0:
        print("Idade inválida! Por favor, digite um número positivo.")
    elif idade <= 12:
        print("Você é uma Criança.")
    elif idade <= 17:
        print("Você é um Adolescente.")
    elif idade <= 59:
        print("Você é um Adulto.")
    else:
        print("Você é um Idoso.")

classificar_idade()