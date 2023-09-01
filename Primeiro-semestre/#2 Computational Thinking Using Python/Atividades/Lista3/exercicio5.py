idade_dias = int(input("Digite a idade em dias: "))
idade_meses = int(input("Digite a idade em meses: "))
idade_anos = int(input("Digite a idade em anos: "))

total = (idade_anos * 365) + (idade_meses * 30) + idade_dias

print(f"Você viveu {total} dias!")
