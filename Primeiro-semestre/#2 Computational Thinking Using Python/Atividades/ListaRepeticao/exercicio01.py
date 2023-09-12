'''
O jogo do PIM era uma brincadeira conhecida do Silvio Santos em seu programa de auditório que
 consistia em pedir a alguém que recite uma sequência numérica iniciada em 1 e caso o
 número seja múltiplo de quatro deveria substitui-lo pela palavra PIM.
 Faça um programa que escreva na tela uma sequência de 1 a 30 substituindo os múltiplos de quatro pela palavra PIM.
'''


for cont in range(1,31):
    if cont % 4 == 0:
        print("PIM")
    else:
        print(cont)
