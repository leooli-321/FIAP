import random

# Abra o arquivo 'palavras.txt' e leia todas as linhas em uma lista
with open(r'C:\Users\Leo Oli\Desktop\Faculdade\FIAP\Primeiro-semestre\#2 Computational Thinking Using Python\Atividades\outros\palavras.txt', encoding='utf-8') as f:
    linhas = f.read().splitlines()

# Escolha uma palavra aleatória da lista
palavra = random.choice(linhas)

print(f"Palavra aleatória: {palavra}")

letras = len(palavra)
tentativas = letras + 3

print(f"A palavra possui {letras} letras, você terá {tentativas} tentativas")

# Crie uma lista para armazenar as letras que o usuário já digitou
letras_digitadas = []

# Crie uma variável para armazenar a palavra oculta
palavra_oculta = ""

# Inicie um loop while para repetir até o usuário ganhar ou perder
while True:
    # Mostre a palavra oculta atualizada
    print(f"Palavra oculta: {palavra_oculta}")

    # Peça ao usuário para digitar uma letra em maiúscula
    decisao = input("\nQual letra você escolhe? [A-Z]\n").upper()

    # Verifique se o usuário já digitou essa letra
    if decisao in letras_digitadas:
        print("Você já digitou essa letra")
    else:
        # Adicione a letra à lista de letras digitadas
        letras_digitadas.append(decisao)

        # Verifique se a letra está na palavra
        if decisao in palavra:
            print("Você acertou uma letra! ")
            # Aumente o número de tentativas em 1
            tentativas += 1
        else:
            # Reduza o número de tentativas em 1
            tentativas -= 1
            print("Você errou a letra")

    # Mostre o número de tentativas restantes
    print(f"Tentativas restantes: {tentativas}")

    # Atualize a palavra oculta com as letras acertadas ou traços
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_digitadas:
            palavra_oculta += letra + " "
        else:
            palavra_oculta += "_ "

    # Verifique se o usuário ganhou ou perdeu o jogo
    if "_" not in palavra_oculta:
        print("Você ganhou o jogo!")
        break
    if tentativas == 0:
        print("Você perdeu o jogo!")
        break
