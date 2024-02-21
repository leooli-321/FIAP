# CRUD = (inserir, alterar, remover ou exibir) de uma lista de dicionarios com dados de alunos

def main():
    resp = "S"
    lista_alunos = []

    while (resp != "N" or "n"):
        print("1 = Inserir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Excluir Aluno")
        print("4 - Exibir Alunos")
        opc = int(input("Digite a opção desejada: (1-4)"))

        match opc:

            case 1:
                inserir_aluno(lista_alunos)

            case 2:
                rm = int(input("Digite o RM do aluno a ser alterado: "))
                indice = buscar_aluno(lista_alunos, len(lista_alunos), rm)
                if indice != -1:
                    alterar_aluno(lista_alunos, indice)
                else:
                    print("Rm do aluno não encontrado!")
                    
            case 3:
                rm = int(input("Digite o RM do aluno a ser alterado: "))
                indice = buscar_aluno(lista_alunos, len(lista_alunos), rm)
                if indice != -1:
                    alterar_aluno(lista_alunos, indice)
                else:
                    print("Rm do aluno não encontrado!")

            case 4:
                exibir_alunos(lista_alunos, len(lista_alunos))

            case _:
                print("Opção inválida!")
        resp = input("Deseja continuar? [S/N]")


def inserir_aluno(lista_alunos):
    rm = int(input("\nDigite o RM do aluno: "))
    nome = input("Digite o nome do aluno: ")
    curso = input("O que este aluno está cursando? ")
    disc = input("Digite a disciplina: ")
    nmrFaltas = int(input("Digite a quantidade de faltas do aluno: "))
    aluno = {'RM': rm, 'Nome': nome,  'Curso': curso,
             'Disciplina': disc, 'numerodeFaltas': nmrFaltas}
    lista_alunos.append(aluno)


def buscar_aluno(lista_alunos, tam, rm):
    indice = -1
    for i in range(tam):
        if lista_alunos[i]['RM'] == rm:
            indice = i
    return (indice)


def alterar_aluno(lista_alunos, indice):
    print(f"Nome do aluno: {lista_alunos[indice]['Nome']}")
    lista_alunos[indice]['Nome'] = input("Digite o novo nome: ")

    print(f"Curso do aluno: {lista_alunos[indice]['Curso']}")
    lista_alunos[indice]['Curso'] = input("Digite o novo Curso: ")

    print(f"Disciplina do aluno: {lista_alunos[indice]['Disciplina']}")
    lista_alunos[indice]['Disciplina'] = input("Digite a nova Disciplina: ")

    print(f"Faltas do aluno: {lista_alunos[indice]['numerodeFaltas']}")
    lista_alunos[indice]['numerodeFaltas'] = int(
        input("Digite o novo número de faltas: "))


def excluir_aluno(lista_alunos, indice):
    lista_alunos.pop(indice)
    print("Aluno excluído com sucesso!")


def exibir_alunos(lista_alunos, tam):
    for i in range(tam):
        print(f"ALUNO {i+1}")
        for chave, valor in lista_alunos[i].items():
            print(f"{chave} : {valor}")
        print("--")*15


if __name__ == "__main__":
    main()
