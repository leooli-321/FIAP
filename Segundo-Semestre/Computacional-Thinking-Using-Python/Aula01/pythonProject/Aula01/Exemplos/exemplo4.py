def verificar_paridade(num):
    if num % 2 == 0:
        return True
    else:
        return False

#chamada da função
num = int(input("Digite um número: "))
retorno = verificar_paridade((num))
