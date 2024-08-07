# Entrada de dados
numeros = [10, 5, 7, 4, 6, 3, 8]

# Classifica em ordem descrescente
numeros.sort(reverse = True)

for numero in numeros:
    print(numero, end=' ')

media = sum(numeros)/len(numeros)

print(f'\n Resultado da média: {media:,.2f}.')

