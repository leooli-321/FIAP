# Tratamento de erros

# 2 > Tratamento de divisão por zero

try:
    num1 = int(input('Digite o primeiro número:\n'))
    num2 = int(input('DIgite o segundo número:\n '))

    divisao = num1 / num2
except ZeroDivisionError and ValueError:
    print('Não existe divisão por zero.')
# except ValueError:
#     print('Digite dados numéricos')
else:
    print(f'A divisão de {num1} por {num2} é: {divisao}')
finally:
    print('Operação finalizada')
