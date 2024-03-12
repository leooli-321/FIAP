# Criar uma lista com os IPVAs dos veículos de acordo com os valores e os tempos de fabricação

listaValores = [7500, 5600, 7800, 20400, 6900, 7650]
listaIdades = [4, 3, 22, 25, 2, 23]

listaIPVAs = list(map(lambda valor, idade: valor *
                  0.04 if (idade < 20) else 0, listaValores, listaIdades))

print(listaIPVAs)
