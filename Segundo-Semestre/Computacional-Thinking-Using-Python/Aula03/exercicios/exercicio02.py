def main():
    lista_notas = []
    tam = int(input("Quantos alunos há na sala?\n "))
    ler_lista(lista_notas, tam)
    print(f"A média das notas é {calcular_media_notas(lista_notas):.1f}")
    print(f"Lista com notas acima de 7: {criar_lista_notas_maior_sete(lista_notas)}")


def ler_lista(lista_notas, tam):
    for i in range(tam):
        lista_notas.append(float(input('Digite a nota do aluno: ')))


def calcular_media_notas(lista_notas):
    soma = sum(lista_notas)
    qtde_elementos = len(lista_notas)
    media = soma / qtde_elementos
    return (media)


def criar_lista_notas_maior_sete(lista_notas, tam):
    lista_acima_sete = []
    for i in range(tam):
        if (lista_notas[i] > 7.0):
            lista_acima_sete.append(lista_notas[i])
    return (lista_acima_sete)


if __name__ == "__main__":
    main()
