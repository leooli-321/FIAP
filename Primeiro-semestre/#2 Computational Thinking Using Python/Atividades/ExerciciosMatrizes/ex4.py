matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Insira um número para o índice: [{linha}, {coluna}]: "))

somas = [0, 0, 0]
for linha in range(0, 3):
    somas[linha] = sum(matriz[linha])

maior_soma = max(somas)
linha_maior_soma = somas.index(maior_soma) + 1

print(f"A matriz é: {matriz}")
print(f"A linha de maior soma é a linha {linha_maior_soma} com a soma {maior_soma}")
