'''
Construa um programa em Python para preencher uma matriz, de 6 linhas por 6 colunas, com elementos do tipo int.
 Em seguida, o programa deve apresentar, na tela, todos os elementos pares contidos na matriz,
  bem como a posição em que eles se encontram.
'''

matriz = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        matriz[linha][coluna] = int(input(f'Insira um número para o índice: [{linha}, {coluna}]: '))

print()
print('*' * 60)
print()

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        print(f'[{matriz[linha][coluna]:^6}]', end='')
    print()

print()
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        if matriz[linha][coluna] % 2 == 0:
            print(f'Par encontrado no índice: [{linha}, {coluna}]')
