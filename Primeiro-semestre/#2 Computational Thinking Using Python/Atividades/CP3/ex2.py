def funcao_a(x):
    s = 0
    for i in x:
        s += int(i)
    return s

rm = input('Informe seu RM: ')
'rm553759'

resultado = funcao_a(rm)
print(resultado)
