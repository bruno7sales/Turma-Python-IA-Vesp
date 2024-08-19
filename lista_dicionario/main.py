# Lista de Dicionario
chaves = ('Nome', 'Idade', 'Profissão')

usuarios = [
    {
        chaves[0]: 'Fulano',
        chaves[1]: 20,
        chaves[2]: 'Programador'
    },
    {
        chaves[0]: 'Cicrano',
        chaves[1]: 35,
        chaves[2]: 'Analista'
    },
    {
        chaves[0]: 'Beltrano',
        chaves[1]: 45,
        chaves[2]: 'Faxineiro'
    }
]
print(f'{'=' * 10} LISTA DE USUÁRIOS{'=' * 10}\n')

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
    
    print(f'\n{'='*10}\n')

# Adiconar novo usuario
usuarios = []

for i in range(len(chaves)):
    usuario[chave[i]] = input(f'Informe o/a {chaves[i]}: ')
    
usuarios.append(usuario)

print(f'\nUsuário cadastrado com sucesso!')

print(f'{'=' * 10} LISTA DE USUÁRIOS{'='*10}\n')

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
    
    print(f'\n{'='*10}\n')

