numeros = []
par = []
impar = []

while len(numeros) < 10:
    selecao = int(input("Digite 10 números em sequência: "))
    numeros.append(selecao)

    if selecao % 2 == 0:
        par.append(selecao)
    else:
        impar.append(selecao)

print(f"Números digitados: {numeros}")
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")
