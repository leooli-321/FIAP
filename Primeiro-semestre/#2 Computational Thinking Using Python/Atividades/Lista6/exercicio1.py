opcao = int(input("Digite o código do produto: \n"))

match opcao:
    case 1:
        print("01 / Canela / Preço: R$ 1,20")
    case 2:
        print("02 / Lápis /  Preço: R$ 0,80")
    case 3:
        print("03 / Caderno /  Preço: R$ 4,50")
    case 4:
        print("04 / Borracha /  Preço: R$ 1,00")
    case 5:
        print("05 / Régua /  Preço: R$ 1,50")
    case _:
        print("NÚMERO INVÁLIDO")
