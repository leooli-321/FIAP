# 1) Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter os seguintes dados:

# a. Código

# b. Nome do funcionário

# c. Idade do funcionário

# d. Salário do funcionário

# As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).

def main():
    resposta = "s" or "S"
    lista_funcionario = []

    while resposta != "N" or "n":
        print('1 - Inserir Funcionário')
        print('2 - Alterar Funcionário')
        print('3 - Excluir Funcionário')
        print('4 - Exibir Funcionário')

        opc = int(input('Escolha uma opção [1/4]:\n'))

        match opc:

            case 1:
                inserirFuncionario(lista_funcionario)

            case 2:
                codigo = int(
                    input("Insira o código do funcionário a ser alterado: "))
                indice = buscarFuncionario(
                    lista_funcionario, len(lista_funcionario), codigo)
                if indice != -1:
                    alterarFuncionario(lista_funcionario, indice)
                else:
                    print('Código do funcionnário não encontrado!')

            case 3:
                codigo = int(
                    input("Insira o código do funcionário a ser alterado: "))
                indice = buscarFuncionario(
                    lista_funcionario, len(lista_funcionario), codigo)
                if indice != -1:
                    alterarFuncionario(lista_funcionario, indice)
                else:
                    print('Código do funcionnário não encontrado!')

            case 4:
                exibirFuncionarios(lista_funcionario)

            case _:
                print('Opção Inválida!')

    resp = int(input('Deseja continuar? [S/N]'))


def inserirFuncionario(lista_funcionario):
    codigo = int(input("Insira o código do funcionário: "))
    nome = input("Insira o nome do funcionário: ")
    idade = int(input("Insira a idade do funcionário: "))
    salario = float(input("Insira o salário do funcionário: "))

    funcionario = {codigo: 'codigo', nome: 'Nome',
                   idade: 'Idade', salario: 'Salario'}
    lista_funcionario.append(funcionario)


def buscarFuncionario(lista_funcionario, tam, codigo):
    indice = -1
    for i in range(tam):
        if lista_funcionario[i]['codigo'] == codigo:
            indice = i
    return (indice)


def alterarFuncionario(lista_funcionario, indice):
    print(f"Nome do funcionário: {lista_funcionario[indice]['Nome']}")
    lista_funcionario[indice]['Nome'] = input('Digite o novo nome: ')

    print(f"Código do funcionário: {lista_funcionario[indice]['codigo']}")
    lista_funcionario[indice]['codigo'] = input(
        'Digite o novo codigo do funcionário: ')

    print(f"Idade do funcionário: {lista_funcionario[indice]['idade']}")
    lista_funcionario[indice]['idade'] = input(
        'Altere a idade do funcionário: ')

    print(f"Idade do funcionário: {lista_funcionario[indice]['idade']}")
    lista_funcionario[indice]['idade'] = input(
        'Altere a idade do funcionário: ')


def excluir_funcionario(lista_funcionario, indice):
    lista_funcionario.pop(indice)
    print("Funcionário apagado com sucesso!")


def exibirFuncionarios(lista_funcionario, tam):
    for i in range(tam):
        print(f"Funcionário {i+1}")
        for chave, valor in lista_funcionario[i].items():
            print(f"{chave} : {valor}")
        print('-#')*15


if __name__ == "__main__":
    main()
