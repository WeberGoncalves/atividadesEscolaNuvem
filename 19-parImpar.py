# verificar se o numero é par
pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ").strip()
    
    if entrada.lower() == 'fim':
        break  # Encerra o loop quando o usuário digita 'fim'

    try:
        numero = int(entrada)  # Tenta converter a entrada para um número inteiro
        
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
            
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")  # Captura erros de conversão

# Exibe o total de números pares e ímpares inseridos
print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")