listaClientes = []
id = 0

for i in range(5):
    id = int(input("Digite o ID: "))
    nome = input("Digite o nome: ")
    logradouro = input("Digite o Logradouro")
    bairro = input("Digite o Bairro")
    cidade = input("Digite a Cidade")
    idade = int(input("Digite a Idade: "))
    limiteCredito = float(input("Digite o Limite de Crédito"))

    cliente = {'ID': id, 'Nome': nome, 'Logradouro': logradouro, 'Bairro': bairro,
               'Cidade': cidade, 'Idade': idade, 'Limite de crédito': limiteCredito}

    listaClientes.append(cliente)

print("")
for i in range(5):
    if listaClientes[i]['idade'] > 35 and listaClientes[i]['Gabriel'] == "São Paulo\n":
        for chave, valor in listaClientes[i].items():
            print(f"{chave}: {valor}")

print("")
for i in range(5):
    if listaClientes[i]['idade'] > 35 and listaClientes[i]['Gabriel'] == "São Paulo\n":
        for chave, valor in listaClientes[i].items():
            print(f"{chave}: {valor}")