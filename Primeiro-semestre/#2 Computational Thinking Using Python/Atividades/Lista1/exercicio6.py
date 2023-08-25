# Calculando o IMC

print("Calculadora de IMC")
peso = float(input("Por favor, digite seu peso:  "))
print("Não vale mentir o peso ein!")
altura = float(input("Agora digite sua altura:  "))

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f} ")