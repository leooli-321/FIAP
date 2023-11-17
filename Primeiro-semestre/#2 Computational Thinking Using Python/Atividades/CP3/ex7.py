'7 – No script abaixo, qual será o valor final da variável r?'

rm = input('Informe seu RM: ')
'rm = rm553759'

def funcao_f(x=2, y=5, z=7):
    return y * z if x % 2 == 0 else y + z

r = 0  # Defina r antes de usá-lo
r = funcao_f() > funcao_f(int(rm[-1]), int(rm[3]), int(rm[0]))
