nomes = ['Andre', 'Bernado', 'Carlos', 'Danilo', 'Eduardo', 'Fernando', 'Gabriel', 'Heitor', 'Igor', 'João']


for i in range(len(nomes)):
    print(f'Nome{i+1}: {nomes[i]}')


indice = int(input('Informe um numero do indice: '))

nome = nomes.pop(indice - 1)

print(f'O nome separado foi {nome}')