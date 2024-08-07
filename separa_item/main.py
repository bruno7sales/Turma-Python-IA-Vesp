# Lista de frutas
frutas = ['Maracujá', 'Maçã', 'Lranja', 'Banana','Uva', 'Abacaxi']

# Exibe a lista e os indices na tela
for i in range(len(frutas)):
    print(f'Fruta do indice {i}: {frutas[i]}.')

# Usuario informa o indice do item
indice = int(input('\nInforme o indice do item que deseja separar: '))

# Separe o item
fruta = frutas.pop(indice)

# Exibe o item separado
print(f'\n A furta separada foi: {fruta}\n')
for i in range(len(frutas)):
    print(f'Fruta do indice {i}: {frutas[i]}.')
