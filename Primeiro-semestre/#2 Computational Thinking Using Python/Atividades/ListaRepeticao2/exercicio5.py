n = int(input("Digite o número do fatorial que deseja: "))
fat = 1 # Quando se trata de multiplicação, precisamos iniciar com 1 e não com 0!!!

for i in range(1, n+1):
    fat = fat  * i

print(f"O fatorial de {n} é {fat}")