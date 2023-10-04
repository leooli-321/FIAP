numerosDigitados = []

while True:
    num = int(input("Digite um número positivo: "))
    numerosDigitados.append(num)
    soma = sum(numerosDigitados)

    if num == 0:
        numerosDigitados.pop()
        print(soma)
        menor = min(numerosDigitados)
        print(f"O menor número digitado foi {menor}")
        maior = max(numerosDigitados)
        print(f"O maior número digitado foi {max}")

        break
