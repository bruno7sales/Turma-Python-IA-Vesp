# Lista de compras
compras = ['Ovos', 'Macarrão', 'Feijão', 'Arroz', 'Leite', 'Chocolate']

#Exibir Lista
for i in range(len(compras)):
    print(f'Indice {i}: {compras [i]}.')

# Tratamento de exceções
try:
    # Usuário informa o item que deseja retirar
    indice = int(input('\nIndice do item que deseja retirar: \n'))

    # Retirar item da lista
    del(compras[indice])
    print('\nItem retirado com sucesso.\n')
except:
    print('\nNão foi possivel excluir\n!')
finally:
    for i in range(len(compras)):
        print(f'Indice {i}: {compras[i]}.')
