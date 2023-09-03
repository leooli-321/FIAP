num1 = float(input("Escolha o primeiro número: \n"))
num2 = float(input("Escolha o segundo número: \n"))

print("")
print(f"O que vamos fazer com {num1} e {num2}?")
print("")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Sua opção: "))

match opcao:
    case 1:
        soma = num1 + num2
        print(f"{num1} + {num2} = {soma}!")
    case 2:
        sub = num1 - num2
        print(f"{num1} - {num2} = {sub}!")
    case 3:
        mult = num1 * num2
        print(f"{num1} X {num2} = {mult}!")
    case 4:
        div = num1 / num2
        print(f"{num1} + {num2} = {div}!")
    case _:
        print("OPÇÃO INVÁLIDA")
