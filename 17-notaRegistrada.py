# programa que permita a um professor registrar as notas de uma turma.
def registrar_notas():
    notas = []
    
    while True:
        entrada = input("Digite a nota (ou 'fim' para encerrar): ").strip().lower()
        if entrada == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)  # Armazena apenas o valor numérico
                print(f"Nota registrada: {nota}")
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 0 e 10.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

registrar_notas()