maca = int(input("Bem vindo à mercearia do Braufagélio! \nQuantas maçãs você deseja comprar hoje? "))

if maca >= 12:
    print(f"O total da compra é: {maca},00 reais!")
else:
    taxa = maca * 1.3
    print(f"O total da compra é de: {taxa:.2f} reais!")
