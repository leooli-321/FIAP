import random
import json
import unicodedata


def load_elements(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def normalize_string(s):
    return unicodedata.normalize("NFD", s).casefold()


def play_game():
    score = 0
    total_questions = 10

    elements = load_elements("elements.json")
    keys = list(elements.keys())

    print("Bem-vindo ao jogo de adivinhação dos elementos da tabela periódica!")
    print("Serão {} perguntas. Vamos começar!\n".format(total_questions))

    for _ in range(total_questions):
        random_element = random.choice(keys)
        correct_answer = normalize_string(elements[random_element])

        print("Qual é o elemento químico abreviado por '{}'?".format(random_element))
        user_answer = normalize_string(input("Sua resposta: "))

        if user_answer == correct_answer:
            score += 1
            print("Correto!\n")
        else:
            print("Errado! A resposta correta é '{}'.\n".format(elements[random_element]))

    print("Fim do jogo! Seu placar final é {}/{}.".format(score, total_questions))


play_game()
