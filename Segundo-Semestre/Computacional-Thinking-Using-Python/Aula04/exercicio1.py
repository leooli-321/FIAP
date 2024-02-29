'''
1) Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter os seguintes dados:

a. Código

b. Nome do funcionário

c. Idade do funcionário

d. Salário do funcionário

Faça o tratamento de erros no processo de inserção e alteração. 
As operações deverão ser executadas até que o usuário digite uma opção de saída 0 
(Deseja continuar (1-SIM / 0-NÃO)
'''


def main():
    funcionarios = []
    while True:
        print("1. Adicionar funcionário")
        print("2. Atualizar funcionário")
        print("3. Excluir funcionário")
        print("4. Listar funcionários")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_funcionario(funcionarios)
        elif opcao == '2':
            atualizar_funcionario(funcionarios)
        elif opcao == '3':
            excluir_funcionario(funcionarios)
        elif opcao == '4':
            listar_funcionarios(funcionarios)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


def adicionar_funcionario(funcionarios):
    try:
        codigo = int(input("Digite o código do funcionário: "))
        nome = input("Digite o nome do funcionário: ")
        idade = int(input("Digite a idade do funcionário: "))
        salario = float(input("Digite o salário do funcionário: "))
        funcionarios.append({'Código': codigo, 'Nome': nome,
                            'Idade': idade, 'Salário': salario})
        print("Funcionário adicionado com sucesso.")
    except ValueError:
        print("Erro ao adicionar funcionário. Verifique se os dados foram inseridos corretamente.")


def atualizar_funcionario(funcionarios):
    try:
        codigo = int(
            input("Digite o código do funcionário que deseja atualizar: "))
        for funcionario in funcionarios:
            if funcionario['Código'] == codigo:
                nome = input("Digite o novo nome do funcionário: ")
                idade = int(input("Digite a nova idade do funcionário: "))
                salario = float(
                    input("Digite o novo salário do funcionário: "))
                funcionario.update(
                    {'Nome': nome, 'Idade': idade, 'Salário': salario})
                print("Funcionário atualizado com sucesso.")
                return
        print("Funcionário não encontrado.")
    except ValueError:
        print("Erro ao atualizar funcionário. Verifique se os dados foram inseridos corretamente.")


def excluir_funcionario(funcionarios):
    try:
        codigo = int(
            input("Digite o código do funcionário que deseja excluir: "))
        for funcionario in funcionarios:
            if funcionario['Código'] == codigo:
                funcionarios.remove(funcionario)
                print("Funcionário excluído com sucesso.")
                return
        print("Funcionário não encontrado.")
    except ValueError:
        print("Erro ao excluir funcionário. Verifique se os dados foram inseridos corretamente.")


def listar_funcionarios(funcionarios):
    for funcionario in funcionarios:
        print(funcionario)


if __name__ == "__main__":
    main()
