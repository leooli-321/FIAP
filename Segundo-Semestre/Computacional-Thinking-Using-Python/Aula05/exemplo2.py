# Exemplo com MAP

def main():

    listaOriginal = [1, 2, 3, 4, 5]
    listaQuadrado = []

    listaQuadrado = list(map(calcularQuadrado, listaOriginal))

    print(listaOriginal)
    print(listaQuadrado)


def calcularQuadrado(num):
    return (num**2)


if __name__ == "__main__":
    main()
