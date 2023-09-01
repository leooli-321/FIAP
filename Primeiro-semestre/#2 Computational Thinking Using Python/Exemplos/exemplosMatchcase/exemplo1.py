# Dado um número inteiro (de 1 A 7), exiba os dias da semana:

diaSemana = int(input("Digite um número do dia da semana (1 a 7): \n"))
feira = "- feira"
inicio = "Este dia da semana é:"

match diaSemana:
    case 1:
        print(f"{inicio} Domingo")
    case 2:
        print(f"{inicio} Segunda {feira}")
    case 3:
        print(f"{inicio} Terça {feira}")
    case 4:
        print(f"{inicio} Quarta {feira}")
    case 5:
        print(f"{inicio} Quinta {feira}")
    case 6:
        print(f"{inicio} Sexta {feira}")
    case 7:
        print(f"{inicio} Sábado {feira}")
    case _:
        print("NÚMERO INVÁLIDO")
