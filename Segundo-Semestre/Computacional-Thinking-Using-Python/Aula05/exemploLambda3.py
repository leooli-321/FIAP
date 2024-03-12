# Criar uma função lambda que verifica e retorna o maior numero

retornarMaior = lambda num1, num2 : num1 if (num1> num2) else num2
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print(f'O maior número é {retornarMaior}')