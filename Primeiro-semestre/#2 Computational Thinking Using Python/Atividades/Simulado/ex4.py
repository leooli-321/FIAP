'''
Com a volta das aulas presenciais, a mãe de um aluno do ensino fundamental necessita saber quanto gastará com material escolar. Para fazer uma simulação,
ela foi a uma livraria com o objetivo de simular a compra dos seguintes itens básicos: canetas,
lápis e cadernos. Um ponto a se considerar é que essa livraria está com um programa de desconto de 20% nos preços dos cadernos e 5% nas canetas.
Assim sendo, escreva um programa em Python que solicite as quantidades dos itens, preços e calcule o total da compra simulada.
'''

caneta = float(input(f"Insira quanto gastou em canetas:\n"))
qcaneta = int(input(f"Insira a quantidade de canetas compradas:\n"))

lapis = float(input(f"Insira quanto gastou em lápis:\n"))
qlapis = int(input(f"Insira a quantidade de lápis comprados:\n"))

caderno = float(input(f"Insira quanto gastou em cadernos:\n"))
qcadernos = int(input(f"Insira a quantidade de cadernos comprados:\n"))

canetaDesconto = 0.05
cadernoDesconto = 0.2

totalParcialCaneta = caneta - (caneta * canetaDesconto)
totalParcialCaderno = caderno - (caderno * cadernoDesconto)

subtotalCaneta = caneta * qcaneta
subtotalLapis = lapis * qlapis
subtotalCaderno = caderno * qcadernos

total = subtotalCaderno + subtotalCaneta + subtotalLapis

print(f"O total da compra simulada foi {total}!")
