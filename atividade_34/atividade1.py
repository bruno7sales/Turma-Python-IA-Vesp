# Entrada de dados:
try:
    numero = str(input('Insira um numero qaulquer: ')).replace(',', '.')
    # Convertendo para float:
    numero = float(numero)

    # Imprimindo o numero requisitado
    print(f'\nO numero escolhido foi: {numero}')
    print('\n')

    # Imprimindo o tipo do numero, nesse caso o float
    print(f'O tipo do numero escolhido é: {type(numero)}')

except Exception as e:
    print(f'Não foi possivel realizar a operação.\n{e}.')