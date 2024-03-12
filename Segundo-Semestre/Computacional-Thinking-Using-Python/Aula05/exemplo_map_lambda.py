#Map é uma alternativa para o For
## Exemplo SEM a utilização do MAP

def main():
    listaOgirinal = []
    tam = int(input("Digite o tamanho da lista: "))
    lerLista(listaOgirinal, tam)

    #Criar uma nova lista com os elementos da lista original elevados ao quadrado
    listaQuadrado = []
    for i in range(len(listaOgirinal)):
        listaQuadrado.append(calcularQuadrado(listaOgirinal[i]))

    print(listaOgirinal)
    print(listaQuadrado)

def lerLista(lista,tam):
    for i in range(tam):
        lista.append(int(input("Digite um elmento para lista: ")))


def calcularQuadrado(num):
    return(num**2)


if __name__ == "main":
    main()