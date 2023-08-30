livro = int(input("Qual o valor do livro que está comprando? "))

if livro < 10.00:
    print(f"Você pagará {livro * 0.08}")
elif 10.01 >= livro <= 60.00:
    print(f"Você irá pagar um total de {livro * 0.1}")
else:
    print(f"Você receberá um desconto de 20% e pagará {livro * 0.2}")
