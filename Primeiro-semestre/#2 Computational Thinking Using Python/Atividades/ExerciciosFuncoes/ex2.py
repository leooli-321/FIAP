'''Uma função com um parâmetro x que calcule e mostre o dobro de x.'''


def dobro(x):
    print(f'O dobro é {x * 2}')
    return dobro


valor = int(input('Digite um número: '))
dobro(valor)
