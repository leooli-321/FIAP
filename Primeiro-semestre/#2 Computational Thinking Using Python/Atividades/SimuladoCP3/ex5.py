'''Exercício 1: Escreva um programa Python para criar uma matriz 4x4 e preenchê-la com números de 1 a 16.'''

matriz = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

lin=[]
for linha in range(len(matriz)):
    contador=[]
    for coluna in range(len(matriz)):
         lin.append(int(input("Ponha o valor")))
    matriz.append(linha)



matriz.append(contador)

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
       print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()