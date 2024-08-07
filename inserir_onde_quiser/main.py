# Lista de nomes
nomes = ['Fulano', 'Ciclano', 'Beltrano']

# Usuário insere um novo nome 
novo_nome = input('Informe o novo nome: ').capitalize()
posicao = int(input('Inforne a posição do novo nome: '))

# Insere o novo nome nolcal indicado
nomes.insert(posicao, novo_nome)
print('\n')

# Imprime a lista 
for nome in nomes:
    print(nome)

# Ordena a lista
nomes.sort()
print('\n')


# Exibe a lista ordenada
for nome in nomes:
    print(nome)
