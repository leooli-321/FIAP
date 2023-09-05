# Somatório dos números inteiros de 1 até 10

soma = 0

for cont in range(1,11):
    soma = soma + cont #Soma acumulada. variável adicionada à variável.
    print(f"O valor da soma é {soma}")



# Somatório de 5 números inteiros definidos pelo usuário

somaNumeros = 0
for i in range(5):
    num = int(input("Digite um número inteiro:\n"))
    somaNumeros = somaNumeros + num


print(f"O valor da soma é {somaNumeros}")
