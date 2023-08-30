ano = int(input("Digite um ano: \n"))
bissexto = ano//400

if 1000 >= ano <= 2999:
    print("NÚMERO INVÁLIDO")
if bissexto == 0:
    print("Ano não bissexto!")
else:
    print("Ano bissexto")