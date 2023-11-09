'''Escreva um programa que leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.'''

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
contador10 = 0

for linha in range(0, 4):
    for coluna in range(0, 4):
        matriz[linha][coluna] = int(input(f"Digite um valor para o elemento [{linha}, {coluna}]: "))

        if matriz[linha][coluna] > 10:
            contador10 += 1


print("-=" * 50)

for linha in range(0, 4):
    for coluna in range(0, 4):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print(f"Há {contador10} números maiores que 10!")
