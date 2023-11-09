'''Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
(a) o maior elemento da matriz e sua respectiva posição (linha e coluna);
(b) o menor elemento da matriz e sua respectiva posição.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 6):
    for coluna in range(0, 3):
        matriz[linha][coluna] = float(input(f"Digite um valor para o elemento [{linha}, {coluna}]: "))

maiorElemento = max(max(linha) for linha in matriz)
print(f"O maior elemento é {maiorElemento}")
menorElemento = min(min(linha) for linha in matriz)
print(f"O menor elemento é {menorElemento}")
