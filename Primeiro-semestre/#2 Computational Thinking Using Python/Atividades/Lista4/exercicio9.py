peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura**2)

print(f"Seu IMC é {imc:.2f}: \n")

if imc <= 18.5:
    print("Abaixo do peso")
elif 18.5 > imc <= 24.9:
    print("Peso ideal")
elif imc >= 25:
    print("Acima do peso")
