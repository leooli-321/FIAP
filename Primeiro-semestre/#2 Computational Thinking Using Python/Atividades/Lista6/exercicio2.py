num1 = float(input("Digite um número: \n"))

print("")
print("1 - Adicionar 5")
print("2 - Subtrair 4")
print("3 - Dobrar")

opcao = int(input("Digite a opção desejada (de 1 a 3): \n"))

match opcao:
    case 1:
        soma = num1 + 5
        print(f"A soma de {num1} com 5 é {soma}!")
    case 2:
        sub = num1 - 4
        print(f"4 menos {num1} é {sub}!")
    case 3:
        mult = num1 * 2
        print(f"A multiplicação dos dois números, é {mult} !")
    case _:
        print("OPÇÃO INVÁLIDA")
