'''
    Considerando dois números inteiros, execute uma operação de acordo com o menu abaixo:
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
'''

num1 = int(input("Digite o primeiro número inteiro: \n"))
num2 = int(input("Digite o segundo número inteiro: \n"))

print("")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite a opção desejada (de 1 a 4): \n"))

match opcao:
    case 1:
        soma = num1 + num2
        print(f"A soma do dois números, é: {soma} !")
    case 2:
        sub = num1 - num2
        print(f"A subtração dos dois números, é: {sub} !")
    case 3:
        mult = num1 * num2
        print(f"A multiplicação dos dois números, é {mult} !")
    case 4:
        div = num1 / num2
        print(f"A divisão destes números, é: {div} !")
    case _:
        print("OPÇÃO INVÁLIDA")
