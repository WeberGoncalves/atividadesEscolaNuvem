produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))

print(f"Recibo do produto\n"
      f"Produto: {produto}\n"
      f"Preço: R${preco:.2f}\n"
      f"Quantidade: {quantidade}\n"
      f"Valor total: R${preco * quantidade:.2f}")
       