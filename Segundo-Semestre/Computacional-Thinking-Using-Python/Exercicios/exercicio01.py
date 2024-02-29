'''
Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter os seguintes dados:
 
a. Código
 
b. Nome do funcionário
 
c. Idade do funcionário
 
d. Salário do funcionário
 
Faça o tratamento de erros no processo de inserção e alteração. As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).
'''


def main():
    lista_funcionario = []
    resp = 1

    while (resp != 0):
        print("1 - INSERIR FUNCIONÁRIO")
        print("2 - ALTERAR FUNCIONÁRIO")
        print("3 - EXCLUIR FUNCIONÁRIO")
        print("4 - EXIBIR FUNCIONÁRIOS")
        opc = int(input("Digite a opção desejada: "))

        match opc:

            case 1:
                inseri_funcionario(lista_funcionario)

            case 2:
                try:
                    codigo = int(
                        input("Digite o codigo do funcionário que deseja alterar: "))
                except ValueError:
                    print("Digite valor númerico para o código")
                else:
                    indice = buscar_funcionario(lista_funcionario, codigo)
                    if (indice != -1):
                        alterar_funcionario(lista_funcionario, indice)
                    else:
                        print("Funcionário não encontrado")

            case 3:
                try:
                    codigo = int(
                        input("Digite o codigo do funcionário que deseja excluir: "))
                except ValueError:
                    print("Digite valor númerico para o código")
                else:
                    indice = buscar_funcionario(lista_funcionario, codigo)
                    if (indice != -1):
                        excluir_funcionario(lista_funcionario, indice)
                    else:
                        print("Funcionário não encontrado: ")

            case 4:
                exibir_funcionarios(lista_funcionario)

            case _:
                print("Opção inválida")

        resp = int(input("Deseja continuar (1-SIM/0-NÃO): "))


def inseri_funcionario(lista_funcionario):
    try:
        codigo = int(input("Digite o código do funcionário: "))
        nome = input("Digite o nome do funcionário: ")
        idade = int(input("Digite a idade do funcionário: "))
        salario = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("Digite dados númericos para o código, idade e salário")
    else:
        funcionario = {'Codigo': codigo, 'Nome': nome,
                       'Idade': idade, 'Salario': salario}
        lista_funcionario.append(funcionario)
        print("funcionario inserido com sucesso!!!")
    finally:
        print("Operação finalizada!")


def buscar_funcionario(lista_funcionario, codigo):
    indice = -1
    for i in range(len(lista_funcionario)):
        if (lista_funcionario[i]['Codigo'] == codigo):
            indice = i
    return indice


def alterar_funcionario(lista_funcionario, indice):
    try:
        print(f"Nome: {lista_funcionario[indice]['Nome']}")
        nome = input("Digite o novo nome: ")
        print(f"Idade:{lista_funcionario[indice]['Idade']}")
        idade = int(input("Digite a idade do funcionário: "))
        print(f"Salario: {lista_funcionario[indice]['Salario']}")
        salario = float(input("Digite novo salario: "))
    except ValueError:
        print("Digite dados númericos para idade e salário")
    else:
        lista_funcionario[indice]['Nome'] = nome
        lista_funcionario[indice]['Idade'] = idade
        lista_funcionario[indice]['Salario'] = salario
        print("Dados alterados com sucesso!!!")
    finally:
        print("Operação finalizada!")


def excluir_funcionario(lista_funcionario, indice):
    lista_funcionario.pop(indice)
    print("Funcionario excluido com sucesso!!!")


def exibir_funcionarios(lista_funcionario):
    for i in range(len(lista_funcionario)):
        print(f"ALUNO {i + 1}")
        for chave, valor in lista_funcionario[i].items():
            print(f"{chave}:{valor}")
        print("____________________________________")


if __name__ == "__main__":
    main()
