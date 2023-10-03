# Calculadora (while) - Critério de parada (1- SIM / 0 - NÂO)

resp = 1 # 0 ou 1

while (resp != 0):
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    opc = int(input("Digite a opção desejada (1-3): "))
    match opc:
        case 1:
            soma = num1 + num2
            print(f"Soma: {soma}")
        case 2:
            sub = num1 - num2
            print(f"Subtração: {sub}")
        case 3:
            mult = num1 * num2
            print(f"Multiplicação: {mult}")
        case _:
            print("Opção inválida")

    resp = int(input("Deseja continuar? (1-SIM / 0-NÃO"))