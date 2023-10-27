listaProdutos = []
i = 0

for i in range(5):
    id += 1
    descricao = input("Digite a Descrição: ")
    categoria = input("Digite a categoria: ")
    qtdEstoque = int(input("Digite a quantidade em estoque: "))
    valorCompra = float(input("Digite o valor da compra: "))
    valorVenda = float(input("Digite o valor da venda: "))

    produto = {'ID':id, 'Descricao':descricao, 'Categoria':categoria,
               'Quantidade em Estoque'qtdEstoque, 'Valor da Compra':valorCompra,  'Valor da Venda':valorVenda}

    listaProdutos.append(produto)

print('Relatório de todos os produtos cuja quantidade em estoque seja inferior a 100 unidades\n')

for i in range(5):
    if listaProdutos[i]['Quantidade em Estoque'] > 100:
        for chave,valor in listaProdutos.items():
            print(f"{chave}: {valor}")