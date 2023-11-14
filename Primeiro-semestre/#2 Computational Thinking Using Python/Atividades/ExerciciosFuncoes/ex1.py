'''Uma função com dois parâmetros (a e b) que mostre o maior deles;'''


def maior(a, b):
    if a > b:
        print(f'{a} é maior que {b}!')
    else:
        print(f'{b} é maior que {a}!')


valor1 = int(input('Insira o primeiro valor: '))
valor2 = int(input('Insira o segundo valor: '))

maior(valor1, valor2)
