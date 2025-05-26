def cacularGorjeta(valorConta, porcetagemGojeta):
    provisorio = valorConta * (porcetagemGojeta / 100)
    gorjeta = f"{provisorio:.2f}"
    return gorjeta

print(cacularGorjeta(250,12))