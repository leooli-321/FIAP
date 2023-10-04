num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

numero1 = 0
numero2 = 0

pares = 0
impares = 0

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

for numero in range(numero1, numero2 + 1):
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
