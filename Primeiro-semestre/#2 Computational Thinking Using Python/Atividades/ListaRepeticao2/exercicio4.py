taxaAbatimento = float(input("Digite a taxa de abatimento: "))
nroPrest = int(input("Digite a quantidade de prestações: "))
primeiraPrest = int(input("Digite o valor da primeira prestação: "))

for prest in range(nroPrest): # << O loop irá pegar o número que for digitado na variável
    if prest == 0: # << Primeira iteração do for.
        print(f"Prestação {prest+1}: {primeiraPrest:.2f}")
        valorPrest = primeiraPrest

    else:
        valorPrest = valorPrest - (valorPrest * taxaAbatimento/100)
        print(f"Prestação {prest+1}: {valorPrest:.2f}")