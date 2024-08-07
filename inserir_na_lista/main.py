#Listas
cobras = ['Sucuri', 'Piton', 'Manba Negra', 'Naja']

#exibir a lista original
for cobra in cobras:
    print(cobra)

# Usuario informa o nome da nova cobra
nova_cobra = input('\nInforma o nome da nova cobra: ')

#isnere a nova cobra na lista
cobras.append(nova_cobra)
print('\n')

# Exibe a nova cobra na lista:
for cobra in cobras:
    print(cobra)

#Ordena a lista
cobras.sort()
print('\nLista em ordem alfabetica: \n')

# Exibe a lista ordenada
for cobra in cobras:
   print(cobra)
