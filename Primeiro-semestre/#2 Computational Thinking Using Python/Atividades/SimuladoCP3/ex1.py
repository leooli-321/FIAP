'''Escreva um programa em Python para ler uma matriz 3X6 de números reais.
Em seguida, quando houver números negativos, troque-os pelo número 1.
Por fim, mostre a matriz atualizada.'''

matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 6):
        matriz[linha][coluna] = float(input(f"Insira um número para o índice [{linha}, {coluna}]: "))
        if matriz[linha][coluna] < 0:
            matriz[linha][coluna] = 1

print("-=" * 30)

for linha in range(0, 3):
    for coluna in range(0, 6):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
