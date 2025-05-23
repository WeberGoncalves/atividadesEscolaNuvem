# programa que verifique se uma senha é forte
while True:
    senha = input("Digite uma senha forte ou 'sair' para encerrar: ").strip()
    
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break
    if len(senha) < 8:
        print("Senha fraca: Deve ter pelo menos 8 caracteres.")
        continue
    
    temNumero = False
    for caracter in senha:
        if caracter in "0123456789":
            temNumero = True
            break
    
    if not temNumero:
        print("Sua senha não contém números. Tente novamente.")
        continue  # Permite que o usuário insira uma nova senha

    print("Senha válida e forte!")
    break