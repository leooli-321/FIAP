# Criar uma nova lista com a multiplicação dos elementos correspondentes de duas listas

def calcularMultiplicacao(num, num2):
    return num * num2


lista1 = [1, 2, 3, 4, 5, 6]
print(lista1)

lista2 = [7, 8, 9, 10, 11, 12]
print(lista2)


lista3 = list(map(calcularMultiplicacao, lista1, lista2))
print(lista3)
