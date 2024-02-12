def main():
    lista_numeros = []
    tam = int(input("Digite o tamanho da lista: "))
    ler_lista(lista_numeros, tam)
    print(f"A média dos elementos da lista é {calcular_media_lista (lista_numeros, tam)}")
    print(f'A nova lista (quadrado dos elementos da lista) é: {criar_lista_quadrado(lista_numeros, tam)}')

def ler_lista (lista_numeros, tam):
    for i in range(tam):
        lista_numeros.append(int(input('Digite um elemento da lista: ')))

# Função para somar calcular e retornar a média dos elementos da lista
def calcular_media_lista(lista_numeros, tam):
    soma = 05
    for i in range(tam):
        soma += lista_numeros[i]
    media = soma / tam
    return(media)

#Função para criar e retornar uma nova lista com os elementos da lista_numeros elevados ao quadrado.
def criar_lista_quadrado(lista_numeros, tam):
    lista_quadrado = []
    for i in range(tam):
        lista_quadrado.append(lista_numeros[i]**2)
    return(lista_quadrado)


if __name__ == "__main__":
    main()