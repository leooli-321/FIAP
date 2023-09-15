inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o final do intervalo: "))
somaPares = 0

for i in range(inicio,fim+1):
    if i % 2 == 0:
        somaPares+=i

print(f"A soma dos pares entre {inicio} e {fim} é {somaPares}")
