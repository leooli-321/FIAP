'''Multiplicação de Matrizes: Escreva um programa Python para multiplicar duas matrizes de dimensões fornecidas pelo usuário.'''

matriz1 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
matriz2 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

matriz3 = []

for linha in range(len(matriz1 and matriz2)):
    for coluna in range(len(matriz1 and matriz2)):
        matriz1[linha][coluna] = int(input(f'Insira um número para o índice [{linha}, {coluna}] da PRIMEIRA matriz: '))
        matriz1[linha][coluna] = int(input(f'Insira um número para o índice [{linha}, {coluna}] da SEGUNDA matriz: '))

for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz2)):
            matriz3[i][j] += matriz1[i][k] * matriz2[k][j]

for r in matriz3:
    print(r)

for linha in range(len(matriz1 and matriz2)):
    for coluna in range(len(matriz1 and matriz2)):
        print(f'{matriz3[linha][coluna]:^5}', end='')
    print()
