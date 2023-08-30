nota = int(input("Qual foi a média anual do Braufagélio? "))

if 6 <= nota <= 10:
    print("Ele passou de ano!")
elif nota > 10:
    print("NÚMERO INVÁLIDO")
elif 3.0 <= nota <= 5.9:
    print("Aluno está de exame!")
else:
    print("Aluno reprovado")