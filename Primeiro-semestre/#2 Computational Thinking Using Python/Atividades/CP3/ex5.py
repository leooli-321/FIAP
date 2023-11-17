5 – No script abaixo, qual será o retorno da funcao_d?

import math

# Função: round (<param_1>, <param_2>)
# --> Arredonda o valor do param_1 com a quantidade de casas decimais do param_2

# Função: math.sqrt(<param>)
# --> Calcula a raiz quadrada
rm = input('Informe seu RM: ')
'rm = rm553759'

def funcao_d(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        r1 = (b + math.sqrt(d)) / (2 * a)
        r2 = (b - math.sqrt(d)) / (2 * a)
        return round(r1, 2), round(r2, 2)
    elif d == 0:
        r = -b / (2 * a)
        return round(r, 2)
    else:
        return None

funcao_d(int(rm[-1]), int(rm[0]) * 2, 2)

