# Criar uma nova com os valores dos IPVAS para 6 veiculos

def calcularIPVA(valorVeiculo):
    return(valorVeiculo * 0.04)

listaValores = [37500, 85600, 57800, 120400, 96900, 87650]

listaIPVAs = list(map(calcularIPVA, listaValores))

print(listaIPVAs)