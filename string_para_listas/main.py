# Variaveis
#nome = 'John Connor'

# Separa a string em uma lista
#nome_completo = nome.split(' ')

# Exibe a lista 
#for parte_nome in nome_completo:
#    print(parte_nome, end =' ')

nome = input('Informe o seu nome completo: ')

# Separa as palavras do nome
nome_lista = nome.split(' ')

# Capitular as palavras novas
for i in range(len(nome_lista)):
    nome_lista[i] = nome_lista[i].capitalize() 

# Junta o nome em uma variavel
nome_completo = ' '.join(nome_lista)

# Exibe na tela
print(nome_completo)

