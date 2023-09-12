'''
Escreva um programa que calcule a soma de todos os números pares entre 1 e 20.
'''

soma = 0

for cont in range (1,21):
    if cont % 2 == 0:
        soma = soma + cont #forma mais simplificada

print(f"A soma dos pares de 1 a 20 é: {soma}")
