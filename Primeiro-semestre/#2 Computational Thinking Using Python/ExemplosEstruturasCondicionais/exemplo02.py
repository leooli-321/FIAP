# Verificar se um número inteiro está entre 1 e 10 (inclusive).
# Caso ele esteja, some 2 ao seu valor e exiba na sela; caso contrário,
# multiplique-o por 3 e exiba na tela.


num = int(input("Digite um número inteiro: "))

if (num >= 1 and num <= 10):
    num = num + 2
else:
    num = num * 3
    
print(f"O novo valor do número é {num}")