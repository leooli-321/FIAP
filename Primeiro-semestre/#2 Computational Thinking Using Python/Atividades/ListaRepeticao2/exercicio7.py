numTab = int(input("Digite o número para fazermos a tabuada: \n"))

for cont in range(11):
    tab = numTab * cont
    print(f"{numTab} x {cont} = {tab}")
    