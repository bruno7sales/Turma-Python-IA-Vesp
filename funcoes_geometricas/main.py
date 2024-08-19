# Funções
def mostrar_menu():
    print('1- Calcular quadrilátero.')
    print('2- Calcular triângulo.')
    print('3- Calcular círculo.')
    print('0- Encerrar progama.')

def calcular_quadrilateo(b, h):
    result = b * h
    return result

def calcular_triangulo(b, h):
    result = (b * h)/2
    return result

def calcular_circulo(r):
    result = 3.14 * (r * r)
    return result

while True:
# Progama Principal
    mostrar_menu()
    print('=' * 25)
    opcao = input('Opção desejada: ')

    match opcao:
        case '1':
            b = float(input('Informe o valor da base: ').replace(',', '.'))
            h = float(input('Informe o valor da altura: ').replace(',', '.'))
            print('=' * 40)
            print(f'A área do quadrilatero é: {calcular_quadrilateo(b,h)}.\n')
            continue

        case '2':
            b = float(input('Informe o valor da base: ').replace(',', '.'))
            h = float(input('Informe o valor da altura: ')).replace(',', '.')
            print('=' * 40)
            print(f'A área do triângulo é: {calcular_triangulo(b,h)}.')
            continue

        case '3':
            r = float(input('Informe o valor do raio: ').replace(',', '.'))
            print('=' * 40)
            print(f'A área do circulo é: {calcular_circulo(r)}.')
            continue
        case '0':
            break
