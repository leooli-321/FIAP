
rm = input('Informe seu RM: ')
'rm = rm553759'

def funcao_h(**x):
    n = None
    i = 0
    for k, v in x.items():
        if int(v) > i:
            i = int(v)
            n = k
    return n

funcao_h(a=rm[-1], b=rm[1], c=rm[2], d=rm[3])
