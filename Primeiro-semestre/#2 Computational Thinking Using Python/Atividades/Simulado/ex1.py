'''
O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos
(aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
 escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.
'''

custoFabrica = int(input("\nInsira o Custo de fábrica:\n"))
distribuidor = 0.28
imposto = 0.45

custoDist = custoFabrica * distribuidor
custoIpt = custoFabrica * imposto

total = custoIpt + custoFabrica + custoDist


print(f"\nO valor total para o consumidor é de {total:.2f}!")
