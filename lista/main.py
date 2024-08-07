# Listas
# Ao trabaçhar com listas, coloque as variaveis com nomes no plural
nomes = ['Fulano', 'Ciclano', 'Beltrano', 'Joana', 'Maria']

# Saida de Dados
print(f'Quantidade de nomes: {len(nomes)}.\n')
print('Modo 1: \n')

for nome in nomes:
    print(nome)

for i in  range(5):
    print(f'{i + 1}° nome: {nomes[i]}. ')
