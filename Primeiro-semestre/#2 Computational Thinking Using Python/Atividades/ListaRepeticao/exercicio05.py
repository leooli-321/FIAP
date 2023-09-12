'''
Faça um programa em Python que mostre na tela os números divisíveis por 6 compreendidos entre 50 e 100.
(Considere os números 50 e 100 e utilize estruturas de repetição).
'''

for cont in range(50, 101):
    if cont % 6 == 0:
        print(cont)
        