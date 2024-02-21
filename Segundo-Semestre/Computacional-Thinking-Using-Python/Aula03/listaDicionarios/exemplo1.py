# Criar uma lista de dicionários para armazenar dados de 5 alunos

lista_alunos = []

for i in range(5):
    rm = int(input("\nDigite o RM do aluno: "))
    nome = input("Digite o nome do aluno: ")
    curso = input("O que este aluno está cursando? ")
    disc = input("Digite a disciplina: ")
    nmrFaltas = int(input("Digite a quantidade de faltas do aluno: "))
    aluno = {'RM' : rm, 'Nome': nome,  'Curso': curso, 'Disciplina': disc, 'Número de  Faltas': nmrFaltas}
    lista_alunos.append(aluno)

print(lista_alunos)