# Tratamento de erros: try, except, else, finally

# 1) tratamento de erros de conversão de tipos de dados:

try:  # o python tenta executar as 3 instruções
    nome = input('Digite o nome:\n ')
    cpf = int(input('Digite o CPF:\n '))
    salario = float(input('Digite o salário:\n '))
except ValueError:  # é quando a tentativa é fracassada
    print('Digite dados numéricos para o CPF e salário!')
else:  # é quando a tentativa ocorreu e teve sucesso
    funcionario = {'Nome': nome, 'CPF': cpf, 'Salário': salario}
    print('Dados cadastrados com sucesso!')
finally: # Finalização do tratamento de erros:
    print('Operação finalizada')