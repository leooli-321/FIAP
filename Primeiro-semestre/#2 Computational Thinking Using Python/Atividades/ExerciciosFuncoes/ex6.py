'''uma função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
 O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento.
 O cálculo do valor a ser pago é feito da seguinte forma: para pagamentos sem atraso, cobrar o valor da prestação.
 Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso. A função deverá retornar o valor da prestação.'''


def valorpagamento(v, a):
    if a > 0:
        multa = v * 0.03
        juros = a * 0.001 * v
        total = v + multa + juros
        print(f'\nO valor a ser pago será {total}')
    else:
        print(f'\nO valor a ser pago será {v}')
    return valorpagamento


valor = float(input(f'Digite o valor da prestação: '))
atraso = int(input(f'Digite a quantidade de dias em atraso: '))

valorpagamento(valor, atraso)

