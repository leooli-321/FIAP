mercadoria = int(input("Qual o valor da mercadoria? "))
dinheiro = int(input("Quanto você tem em mãos? "))


if (dinheiro > mercadoria):
    print("Você já pode pagar pelo produto!")
else:
    print("Saldo insuficiente :( ")