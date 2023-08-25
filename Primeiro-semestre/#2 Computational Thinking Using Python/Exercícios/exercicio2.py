# Programa para calcular a média aritmética de 4 avaliações:

av1 = float(input("Digite a nota da primeira avaliação: "))
av2 = float(input("Digite a nota da segunda avaliação: "))
av3 = float(input("Digite a nota da terveira avaliação: "))
av4 = float(input("Digite a nota da quarta avaliação: "))

media = (av1 + av2 + av3 + av4) / 4
print(f"A média do aluno é de: {media:.1f}")