# Funções em listas

listaNomes = ["Maira", "João", "Ana", "Pedro", "Antônio", "José"]
listaNumeros = [4, 6, 10, 5, 9, 8]

## Função que retorna o tamanho da lista (quantidade de elementos)

tamanho = len(listaNomes)
print(f"O tamanho da lista é {tamanho}")

# Função que calcula o somatório dos elementos da lista

somatorio = sum(listaNumeros)
print(f"O somatório da lista é: {somatorio}")

# Função que retorna o índice de um elemento da lista:

nomePessoa = input("Digite o nome a ser procurado: ")
if (nomePessoa in listaNomes):
    indice = listaNomes.index(nomePessoa)
    print(f"{nomePessoa} está no índice {indice}")
else:
    print("O nome não está na lista")