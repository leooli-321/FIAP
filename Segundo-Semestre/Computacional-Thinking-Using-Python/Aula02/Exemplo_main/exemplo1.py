def main():
    resp = "S"

    while (resp != "N"):
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        opc = int(input("Digite a opção desejada (1-4): "))

        match opc:
            case 1:
                num1, num2 = ler_numeros()
                print(f"A soma é {somar_numeros}")
            case 2:
                num1, num2 = ler_numeros()
                print(f"A subtração é {subtrair_numeros}")
            case 3:
                num1, num2 = ler_numeros()
                print(f"A multiplicação é {multiplicar_numeros}")
            case 4:
                num1, num2 = ler_numeros()
                print(f"A divisão é {dividir_numeros}")
            case _:
                print('Opção inválida')

        resp = input('Deseja Continuar? (S/N)')


# Funções do programador:
def ler_numeros():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    return (num1, num2)


def somar_numeros(num1, num2):
    soma = num1 + num2
    return (soma)


def subtrair_numeros(num1, num2):
    sub = num1 - num2
    return (sub)


def multiplicar_numeros(num1, num2):
    mult = num1 * num2
    return (mult)


def dividir_numeros(num1, num2):
    div = num1 / num2
    return (div)


if __name__ == "__main__":
    main()
