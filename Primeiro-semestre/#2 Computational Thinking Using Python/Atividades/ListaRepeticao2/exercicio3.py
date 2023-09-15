nomeEmpresa = input("Digite o nome da empresa: \n")

somaSalarios = 0

for cont in range(5):
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    somaSalarios = somaSalarios + salario

    if (cont == 0 ): # << Primeira leitura das variáveis.
        maiorSalario = salario
        nomeMaiorSalario = nome
        menorSalario = salario
        nomeMenorSalario = nome
    else: # << Leitura do segundo salário em diante.
        if(salario > maiorSalario):
            maiorSalario = salario
            nomeMaiorSalario = nome

        if (salario < menorSalario):
            menorSalario = salario
            nomeMenorSalario = nome

mediaSalarios = somaSalarios / 5

print(f"A média salarial dos funcionários da empresa {nomeEmpresa} é {mediaSalarios:.2f}")
print(f"{nomeMenorSalario} recebe o menor salário: {menorSalario:.2f}")
print(f"{nomeMaiorSalario} recebe o menor salário: {maiorSalario:.2f}")
