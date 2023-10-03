# Percorrer a lista e exebir seus elementos na vertical:

listaNumeros = [4, 3, 7, 8, 10, 15, 20]

tamanho = len(listaNumeros)

for i in range(tamanho):
    print(listaNumeros[i])


    '''
    Duas listas:
    A : 10 números inteiros
    B : 10 números correspondentes aos números da lista A dobrados
    '''

listaA = [3, 7, 5, 8, 2, 1, 10, 14, 15, 18]

# Inserção de elementos na lista:  método 'append'

tamanho = len(listaA)
listaB = [] # << lista vazia

for i in range (tamanho):
    dobro = listaA[i] * 2
    listaB.append(dobro)

print(listaA)
print(listaB)

# Método 'insert' = permite inserir um elemento em um índice pré-determinado

listaB.insert(2, 50)

print(listaB)

# Exclusão de um elemento da lista:

# Método pop (primeira forma: excluir o último da lista)

listaB.pop()
print(listaB)

# Método pop (segunda forma: excluir oir um índice pré-determinado)

listaB.pop(2) # Excluir o elemento no índice 2
print(listaB)


# Método remove (exclui um elemento da lista pelo valor)

listaB.remove(4) # << Excluindo o elemento 4 da lista
print(listaB)
