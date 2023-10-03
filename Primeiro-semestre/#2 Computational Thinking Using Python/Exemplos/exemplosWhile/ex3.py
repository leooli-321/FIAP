## Somatório de 5 números digitados pelo usuário

cont = 1
soma = 0

while cont<=5:
    num = int(input("Digite um número: "))
    soma += num
    cont += 1

print(f"Soma dos números é {soma}")
