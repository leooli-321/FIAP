'''uma função que tenha um parâmetro “n” e que calcule e retorne a média de todos os pares de 1 até N.'''


def calcular(n):
    soma = 0
    contador = 0

    for numero in range(1, n+1):
        if numero % 2 == 0:
            soma += numero
            contador += 1
    media = soma / contador if contador != 0 else 0
    print(f'A média dos números pares entre 1 e {n} é: {media}')


numero = int(input('Insira um número: '))
calcular(numero)
