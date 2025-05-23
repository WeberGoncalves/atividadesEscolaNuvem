peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 24.9:
    classificacao = "Peso normal"
elif imc < 29.9:
    classificacao = "Sobrepeso"
elif imc < 34.9:
    classificacao = "Obesidade grau I"
elif imc < 39.9:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III (mórbida)"

print(f"Seu IMC é {imc:.1f}. Classificação: {classificacao}")