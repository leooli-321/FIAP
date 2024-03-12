# Combinação de MAP e LAMBDA
# Criar uma nova lista onde os pares serão mantidos e os ímpares trocados por 0

listaOgirinal = [5, 8, 4, 6, 9, 13, 1]

listaNova = list(map(lambda num: num if (num % 2 == 0) else 0, listaOgirinal))

print(listaNova)