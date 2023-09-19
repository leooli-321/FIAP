'''
Um grupo de amigos resolveu fazer um happy hour em um bar após o horário de trabalho.
 Na ocasião eles pediram porções de batatas fritas, pastéis e cervejas para acompanhar.
  Escreva um programa em Python que calcule o total do pedido baseado nas quantidades de porções e cervejas consumidas tendo como referência a tabela abaixo.
  Além disso, calcule o valor individual da conta de acordo com o número de amigos.
'''

fritas = 35
pasteis = 25
cerveja = 18

for i in range(3):
    cod = int(input("Digite o código do produto (1-3)"))
    match cod:
        case 1:
            qFritas = int(input("Quantas porções de batatas fritas foram pedidas?\n"))
        case 2:
            qPasteis = int(input("Quantas porções de pastéis foram pedidos?\n"))
        case 3:
            qCervejas = int(input("Quantas cervejas foram pedidas?\n"))
        case _:
            print("Número inválido")

totalFritas = fritas * qFritas
totalPasteis = pasteis * qPasteis
totalCervejas = cerveja * qCervejas

total = totalCervejas + totalPasteis + totalFritas

amigos = int(input("\nQuantos amigos irão dividir a conta?\n"))

print(f"A conta deu {total:.2f}")
print(f"Vocês pagarão {total / amigos:.2f} cada!")
