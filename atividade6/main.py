"""
Crie um programa que receba o valor atual da gasolina e do etanol, 
e verifica qual o melhor combustível para um carro flex abastecer. 
Ao terminar, envie o arquivo .py.

"""

# Entrada de Dados
gasolina_preco = str(input('Digite o preço da Gasolina: ')).replace(',','.')
etanol_preco = str(input('Digite o preço do Etanol: ')).replace(',','.')

# Convertendo Dados (Aceitaram Jesus!! \o/)
gasolina_preco = float(gasolina_preco)
etanol_preco = float(etanol_preco)

# Verificando:
if gasolina_preco * 0.70 < etanol_preco:
    print('A Gasolina está com um preço melhor do que o Etanol!')
else:
    print('O Etanol está com o preço melhor que o da Gasolina!')

