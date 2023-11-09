'''Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal da matriz por um número k.
Imprima a matriz na tela antes e depois da multiplicação.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Insira um número para o índice [{linha}, {coluna}]: "))

print('-=' * 40)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('-=' * 40)

mult = int(input("Agora insira o multiplicador: "))

matriz[0][0] *= mult
matriz[1][1] *= mult
matriz[2][2] *= mult

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
