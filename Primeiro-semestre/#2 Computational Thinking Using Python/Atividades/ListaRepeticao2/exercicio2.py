inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

contaPares = 0
contaImpares = 0

for i in range(inicio,fim+1):
    if i % 2 ==0:
        contaPares = contaPares + 1

    else:
        contaImpares = contaImpares + 1


print(f"Existem {contaPares} entre {inicio} e {fim}! ")
print(f"Existem {contaImpares} entre {inicio} e {fim}! ")
