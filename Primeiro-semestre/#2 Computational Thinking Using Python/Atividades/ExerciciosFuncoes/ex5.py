'''uma função chamada somaImposto, que possua dois parâmetros:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas e deve retornar o custo com o imposto.'''


def somaImposto(taxaImposto, custo):
    custo_com_imposto = custo + (custo * taxaImposto / 100)
    return custo_com_imposto
