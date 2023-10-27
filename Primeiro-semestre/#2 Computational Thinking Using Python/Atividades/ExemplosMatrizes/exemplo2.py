# Solicitar que o usuário digite os números para criar uma matrix 3 x 4

matriz = []

for lin in range(3):
    linha = []
    print(lin)
    for col in range(4):
        linha.append(int(input("Digite um elemento: ")))
        print(f"\t {col}")
    matriz.append(linha)

for i in range(3):
    print(matriz[i])


# Exibir somente os números pares:
for lin in range(3):
    for col in range(4):
        if matriz[lin][col] % 2 == 0:
            print(matriz[lin][col])
