'''
2) Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter os seguintes dados:

a. Código

b. Descrição do produto

c. Quantidade em estoque

d. Valor do produto

Faça o tratamento de erros no processo de inserção e alteração. 
As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).'''


def inserirProduto(lista_produtos):
    codigo = int(input("Insira o código do produto: "))
    descricao = input("Insira a descricao do produto: ")
    quantidade = int(input("Insira a quantidade em estoque: "))
    valor = float(input("Insira o valor do produto: "))

    produto = {codigo: 'Codigo', descricao: 'Descricao',
               quantidade: 'Quantidade', valor: 'Valor'}

    lista_produtos.append(produto)


def buscarProduto(lista_produtos, tam, codigo):
    indice = -1
    for i in range(tam):
        if lista_produtos[i]['codigo'] == codigo:
            indice = i
    return (indice)


def alterarProduto(lista_produto, indice):
    print(f"Descrição do Produto: {lista_produto[indice]['descricao']}")
    lista_produto[indice]['descricao'] = input(
        'Digite a nova descricao do Produto: ')

    print(f"Quantidade do Produto: {lista_produto[indice]['quantidade']}")
    lista_produto[indice]['quantidade'] = input(
        'Altere a quantidade do Produto: ')

    print(f"Valor do Produto: {lista_produto[indice]['valor']}")
    lista_produto[indice]['valor'] = input(
        'Altere o valor do Produto: ')


def excluir_produto(lista_produto, indice):
    lista_produto.pop(indice)
    print("Produto excluído.")


def exibir_produtos(lista_produtos):
    for i in range(len(lista_produtos)):
        print(f"ALUNO {i + 1}")
        for chave, valor in lista_produtos[i].items():
            print(f"{chave}:{valor}")
        print("---" * 15)
