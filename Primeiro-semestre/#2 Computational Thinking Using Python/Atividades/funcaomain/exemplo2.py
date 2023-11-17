'''
Exemplo:
    - função que carrega uma lista de números inteiros
    - função que calcule e retorne uma lista com os valores da lista original, elevados ao quadrado
'''


def main():
    lista = []
    tamanho = int
    carregar_lista(lista, tamanho)
    print(f'A lista quadrados é {calcular_listaquadrados(lista)}')


def carregar_lista(lista, tamanho):
    for i in range(tamanho):
        lista.append(int(input('Digite um elemento da lista: ')))
        

def calcular_listaquadrados(lista):
    lista_quadrados = []
    for i in range(len(lista)):
        lista_quadrados.append((lista[i0**2]))
    return lista_quadrados


if __name__ == "__main__":
    main()
