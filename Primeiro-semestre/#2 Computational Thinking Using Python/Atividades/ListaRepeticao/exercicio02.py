'''
Escreva um programa que faça a leitura das notas dos 3 checkpoints de 15 alunos
e mostre a média dos checkpoints para cada aluno.
'''


for i in range(3):
    cp1 = float(input("Digite a nota do CP1"))
    cp2 = float(input("Digite a nota do CP2"))
    cp3 = float(input("Digite a nota do CP3"))
    media = (cp1 + cp2 + cp3) / 3
    print(f"Média do aluno {i+1}: {media:.1f}")
    