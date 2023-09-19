nome = input("Digite o nome do funcionário: ")
salarioBruto = float(input("Digite o salário bruto do funcionário: "))

if salarioBruto <= 1100.00:
    descINSS = salarioBruto * 0.075
elif salarioBruto <= 2203.48:
    descINSS = salarioBruto * 0.09
elif salarioBruto <= 3305.22:
    descINSS = salarioBruto * 0.12
elif salarioBruto <= 6433.57:
    descINSS = salarioBruto * 0.14
else:
    print("Não foi possível calcular o desconto para este valor")

print(f"O valor do desconto do INSS é {descINSS:.2f}")
