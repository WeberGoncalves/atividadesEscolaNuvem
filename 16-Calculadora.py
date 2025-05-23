def calcular(num1, num2, operacao):
    try:
        if operacao == '+':
            return num1 + num2
        elif operacao == '-':
            return num1 - num2
        elif operacao == '*':
            return num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Erro: divisão por zero não é permitida.")
            return num1 / num2
        else:
            raise ValueError("Erro: operação inválida.")
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    return None

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        resultado = calcular(num1, num2, operacao)
        if resultado is not None:
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            break
    except ValueError:
        print("Erro: entrada inválida. Certifique-se de digitar números válidos.")