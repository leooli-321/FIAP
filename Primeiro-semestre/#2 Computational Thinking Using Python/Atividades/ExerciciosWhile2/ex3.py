'''Escreva um programa que contenha o seguinte menu:

Opção 1: Verificar e exibir se um número x é ou não divisível por 6;

Opção 2: Calcular o fatorial do número x;

Opção 3: Exibir todos os inteiros de 1 até um número x.

O programa deverá solicitar ao usuário a leitura de um número x e a opção desejada até que o usuário digite “N” para encerrar o programa.
 OBS: o programa deverá solicitar o número e a opção enquanto o usuário digitar“S”.'''

while True:
    decisao = input("\nDeseja começar? [S/N]\n").strip().lower()

    if decisao == "n":
        print("Muito obrigado por calcular conosco!")
        break

    elif decisao != "s":
        print("Opção inválida")
        continue

    print("Opção 1: Verificar e exibir se um número x é ou não divisível por 6")
    print("Opção 2: Calcular o fatorial do número x")
    print("Opção 3: Exibir todos os inteiros de 1 até um número x")
    opcao = int(input("\nSelecione uma opção:"))

    match opcao:
        case 1:
            numero = int(input("Digite um número: "))
            divisivel = numero % 6
            if divisivel > 0:
                print("O número é divisível por 6!")
            else:
                print("O número não é divisível por 6!")

        case 2:
            numero = int(input("Digite um número: "))
            resultado = 1
            for i in range(1, numero+1):
                resultado *= i
            print(f"O fatorial de {numero} é {resultado}!")

        case 3:
            numero = int(input("Digite um número: "))
            total = numero - 1
            print(f"A quantidade de números inteiros entre 1 e {numero}: {total}!")
