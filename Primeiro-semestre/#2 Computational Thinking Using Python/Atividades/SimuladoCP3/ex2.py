'''Escreva um programa em Python que leia uma matriz M [5x5]
e, a cada linha, multiplique cada elemento pelo valor do elemento inserido na diagonal principal da linha.
 Os elementos da matriz serão fornecidos pelo usuário. Escrever a matriz M lida e a matriz M modificada.'''

m = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for linha in range(0, 5):
    for coluna in range(0, 5):
        m[linha][coluna] = int(input(f'Insira um número para o índice [{linha}, {coluna}]'))
        