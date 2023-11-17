
rm = input('Informe seu RM: ')
'rm = rm553759'
def funcao_i(a, b=3.14, *c, **d):
    return int(a) * b + int(c[-1]) % len(d)

funcao_i(rm[4], 2, rm[-1], rm[2], rm[3], rm[0], x=rm[1], y=rm[2])
