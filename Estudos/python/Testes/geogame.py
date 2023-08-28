import random
import json


def fazer_pergunta(pergunta, resposta_correta):
    resposta_usuario = input(pergunta + " ").strip().lower()
    resposta_correta = resposta_correta.lower()

    if resposta_usuario == resposta_correta:
        print("Resposta correta!\n")
        return True
    else:
        print(f"Resposta incorreta. A resposta correta é: {resposta_correta}\n")
        return False


def main():
    print("Bem-vindo ao Jogo de Perguntas sobre Tipos de Rochas Geológicas!\n")
    pontuacao = 0

    with open("perguntas.json", "r") as arquivo:
        dados = json.load(arquivo)
        perguntas = dados["perguntas"]

    random.shuffle(perguntas)

    for pergunta_obj in perguntas:
        pergunta = pergunta_obj["pergunta"]
        resposta_correta = pergunta_obj["resposta"]
        if fazer_pergunta(pergunta, resposta_correta):
            pontuacao += 1

    print(f"Você respondeu corretamente a {pontuacao} de {len(perguntas)} perguntas.")


if __name__ == "__main__":
    main()
