'''

Exemplo:
    - função que carrega uma lista de números inteiros
    - função que calcule e retorne a soma dos impares da lista

'''


def main():
    lista = []
    tamanho = int(input('Digite o tamanho da lista: '))
    carregar_lista(lista, tamanho)
    print(f'A soma dos ímpares da lista é: {calcular_somaimpares(lista)}')


def carregar_lista(lista, tamanho):
    for i in range(tamanho):
        lista.append(int(input('Digite um elemento da lista: ')))


def calcular_somaimpares(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            soma += lista[i]
    return soma


if __name__ == "__main__":
    main()
