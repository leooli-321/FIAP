'''Uma função que calcule e mostre o quadrado de um parâmetro b.'''

print('\nDigite 0 para sair')
while True:
    def quadrado(b):
        print(f'O quadrado de {b} é {b**2}')
        return quadrado


    numero = int(input('\nDigite um número: '))
    quadrado(numero)

    if numero == 0:
        break
