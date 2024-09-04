peso_bebe = str(input('Informe (em gramas) o peso do bebê: ')).replace(',', '.')

#Transformando de string para um float
peso_bebe = float(peso_bebe)
#Logica:

if (peso_bebe < 2500):
    print('O bebê deverá ser internado!')
else:
    print('Parabéns, o bebê encontra-se em um estado de peso saudavel.')
