'''Uma função com um parâmetro n que verifique e mostre se ele é par ou ímpar;'''

print('Digite 0 para sair')

while True:
    def impapar(n):
        if n % 2 == 0:
            print(f'{n} é par')
        else:
            print(f'{n} é impar')
        return impapar


    numero = int(input(f'Digite um número: '))
    impapar(numero)

    if numero == 0:
        break
