# Entrada de Dados
nome = input('Informe seu nome: ')
idade = int(input('Informe sua indade: '))
altura = str(input('Ingorme sua altura: ')).replace(',', '.')

#Convertendo para float
altura = float(altura)

# Verificando altura
if idade >= 12 and altura >= 1.10:
    print(f'{nome} está autorizado.')
else: 
    print(f'{nome} não está autorizado.')

