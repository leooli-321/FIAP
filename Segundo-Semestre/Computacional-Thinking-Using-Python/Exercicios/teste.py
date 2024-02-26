print('\nVamos efetuar o seu cadastro!\n')
nome = input('Digite seu nome:\n')
print('\nComo você se identifica?')
print('[1] - Homem')
print('[2] - Mulher')
print('[3] - Não-Binário')

identidade = int(
    input('\nDigite o número correspondente à sua identidade de gênero:\n'))


def genero(identidade):
    match identidade:
        case 1:
            print(f'\nSeja bem-vindo {nome}!')
        case 2:
            print(f'\nSeja bem-vinda {nome}!')
        case 3:
            print(f'\nSeja bem-vinde {nome}!')
        case _:
            return '\nEntrada inválida'


genero(identidade)

while True:
    idade = int(input(f'\nPor favor {nome}, digite sua idade: \n'))
    print('\nDesculpe, já existe outro usuário com esta idade')
    print('\nDeseja tentar de novo?')
    resposta = input('[S/N]:\n')
    if resposta.lower() == 'n':
        break

print('Cadastro finalizado!')
