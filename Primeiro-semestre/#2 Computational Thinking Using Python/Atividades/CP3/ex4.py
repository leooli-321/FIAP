def funcao_c(x, y):
    m = 0
    while not x + m > y:
        m += 1
    return m

rm = input('Informe seu RM: ')
'rm553759'
resultado = funcao_c(int(rm[-1]), int(rm[0]))
print(resultado)
