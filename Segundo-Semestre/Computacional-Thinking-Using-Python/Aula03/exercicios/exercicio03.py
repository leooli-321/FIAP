def main():
    lista_palavras = []
    tam = int(input("Digite o tamanho da lista de palavtas: "))
    ler_lista(lista_palavras, tam)
    print(f"Existem {contarPalindromos_lista(lista_palavras,tam)} palavras com palíndromo")


def ler_lista(lista_palavras, tam):
    for i in range(tam):
        lista_palavras.append(input("Digite uma palavra da lista: "))

def contarPalindromos_lista(lista_palavras, tam):
    qtde_palindromo = 0
    for i in range(tam):
        if (lista_palavras[i] == lista_palavras[i][::-1]):
            qtde_palindromo+=1
        return  qtde_palindromo
    
if __name__ == "__main__":
    main()