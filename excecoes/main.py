# Entrada de Dados
x = input('Informe um número: ')
y = input('Informe outro número: ')

# Tratamento de Erros
try:  
    multiplicacao = int(x) * int(y)
    print(f'O resultado é {multiplicacao}.')

except:
    print('Não foi possivel realizar o calculo')

