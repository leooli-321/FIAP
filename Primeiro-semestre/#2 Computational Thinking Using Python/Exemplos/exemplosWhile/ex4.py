# Média de todos os números positivos digitados pelo usuário

soma = 0
qtdeNumeros = 0

num = int(input("Digite um número: "))

while (num >= 0):
    soma += num
    qtdeNumeros+=1

media = soma / qtdeNumeros

print(f"A média é {media:.2f}")
