produtos = {'Arroz': 5.99, 'Feijão': 8.49, 'Macarrão': 3.79, 'Óleo': 6.99}
soma = 0

for item in produtos:
    print(item, produtos[item])

for valor in produtos.values():
    soma += valor

print(f"Total da compra: R$ {soma:.2f}")
