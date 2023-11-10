'''faça uma matriz onde receba numeros digitados pelos usuarios, em seguida,
faça uma lista que receba a soma dos números impares de cada coluna da matriz criada.'''

matriz = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

lista = [0, 0, 0, 0, 0, 0]
impar = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        matriz[linha][coluna] = int(input(f'Digite um número para o índice: [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 1:
            lista[coluna] += matriz[linha][coluna]

print()
print('-=' * 40)

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print(lista)
