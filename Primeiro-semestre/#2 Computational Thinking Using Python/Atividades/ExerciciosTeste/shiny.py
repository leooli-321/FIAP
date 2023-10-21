import random

tentativas = 1

while True:
    aleatorio = random.randint(1, 8192)
    catch = random.randint(1, 8192)
    print(aleatorio)

    if aleatorio == catch:
        print(f"Você capturou em {tentativas} tentativas!")
        break

    elif aleatorio != catch:
        tentativas = tentativas + 1
