votosBrancos = int(input("Digite a quantidade de votos brancos: \n"))
votosNulos = int(input("Digite a quantidade de votos nulos: \n"))
votosValidos = int(input("Digite a quantidade de votos válidos: \n"))
totalEleitores = votosBrancos + votosNulos + votosValidos

percBrancos = (votosBrancos * 100) / totalEleitores
percNulos = (votosNulos * 100) / totalEleitores
percValidos = (votosValidos * 100) / totalEleitores

print(f"Percentual de votos em branco, são de: {percBrancos}%")
print(f"Percentual de votos nulos, são de: {percNulos}%")
print(f"Percentual de votos válidos, são de: {percValidos}%")

