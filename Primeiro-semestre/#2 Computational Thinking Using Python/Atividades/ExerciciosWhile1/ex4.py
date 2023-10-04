senha = "1234"
print("Tente adivinhar a senha de 4 dígitos!")

while True:
    tentativa = input("Digite a senha: ")

    if tentativa == senha:
        print("Você acertou!")
        break
    else:
        print("Você errou, tente novamente! \n")

