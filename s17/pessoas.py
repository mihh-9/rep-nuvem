def determinar_sala():
    num_pessoas = int(input("Digite o número de pessoas: "))
    tipo_reuniao = input("Digite o tipo de reunião (normal/executiva): ").lower()

    if num_pessoas <= 0:
            print("Número de pessoas inválido.")
            return

    if tipo_reuniao not in ("normal","executiva"):
            print("Tipo de reunião inválido. Use 'normal' ou 'executiva'.")
            return

    if num_pessoas >=1 and num_pessoas <= 5:
            sala = "pequena"
            print(f"sala {sala}")
    elif num_pessoas >= 6 and num_pessoas <= 15:
            sala = "média"
            print(f"sala {sala}")
    elif num_pessoas > 15 or tipo_reuniao == "executiva":
            sala = "grande"
            print(f"sala {sala}")

        

determinar_sala()