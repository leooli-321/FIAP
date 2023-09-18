nomePessoa1 = input("Digite o nome da primeira pessoa:\n")
alturaPessoa1 = float(input("Digite a altura da primeira pessoa:\n"))

print("")

nomePessoa2 = input("Digite o nome da segunda pessoa:\n")
alturaPessoa2 = float(input("Digite a altura da segunda pessoa:\n"))

print("")

if alturaPessoa1 > alturaPessoa2:
    print(f"{nomePessoa1} é mais alta que {nomePessoa2} !")
else:
    print(f"{nomePessoa2} é mais alta que {nomePessoa1} !")
