hora = 5.00
tempo = int(input("Quantas horas você permaneceu no estacionamento? "))

permanencia = tempo*hora

if permanencia <= 35.00:
    print(f"O total a se pagar é 35 reais!")
else:
    print(f"Você precisa pagar {permanencia} reais!")