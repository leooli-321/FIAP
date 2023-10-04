totalNotas = []
while True:
    notasIndividuais = float(input("Digite a nota do aluno (ou um número negativo para encerrar): "))
    if notasIndividuais < 0:
        break

    totalNotas.append(notasIndividuais)

if totalNotas:
    media = sum(totalNotas) / len(totalNotas)

    if media < 3.5:
        print(f"Média: {media:.2f} = Reprovados direto")
    elif 3.5 <= media < 7:
        print(f"Média: {media:.2f} = Exame")
    else:
        print(f"Média: {media:.2f} = Aprovados")
else:
    print("Nenhuma nota foi inserida.")
